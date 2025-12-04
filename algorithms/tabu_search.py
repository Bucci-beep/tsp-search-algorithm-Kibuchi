import numpy as np
from typing import Tuple, List
from algorithms.neighbourhood import generate_all_swap_moves
from algorithms.two_opt import generate_two_opt_neighbours
from algorithms.tsp_core import tour_length


def tabu_search(
    initial_tour: np.ndarray,
    dist_matrix: np.ndarray,
    tabu_tenure: int = 10,
    max_iterations: int = 200,
    neighbourhood: str = "swap",
    adapt_step: int = 20,
    tenure_min: int = 5,
    tenure_max: int = 25,
    sample_size: int = 300,
) -> Tuple[np.ndarray, float, List[float]]:
    """
    Tabu Search for TSP with:
    - swap or 2-opt neighbourhood
    - adaptive tabu tenure
    - randomised neighbourhood subset (candidate list)

    Parameters
    ----------
    initial_tour : np.ndarray
        Starting solution (permutation of city indices).
    dist_matrix : np.ndarray
        Precomputed distance matrix.
    tabu_tenure : int
        Initial tabu tenure (will adapt).
    max_iterations : int
        Maximum number of iterations.
    neighbourhood : str
        'swap' or '2opt'.
    adapt_step : int
        How often to adapt the tabu tenure (in iterations).
    tenure_min, tenure_max : int
        Bounds for adaptive tenure.
    sample_size : int
        Number of neighbours to sample from the full neighbourhood.

    Returns
    -------
    best_tour, best_cost, history
    """

    n = len(initial_tour)
    current_tour = initial_tour.copy()
    current_cost = tour_length(current_tour, dist_matrix)

    best_tour = current_tour.copy()
    best_cost = current_cost

    history = [best_cost]

    # Tabu list on city-pairs (city indices, not positions)
    tabu_list = np.zeros((n, n), dtype=int)

    last_improvement = 0

    for iteration in range(max_iterations):

        # === 1. Generate neighbourhood ===
        if neighbourhood == "swap":
            # list of (i, j, new_tour)
            full_moves = generate_all_swap_moves(current_tour)
        elif neighbourhood == "2opt":
            # only tours; no detailed move info, we don't use tabu for 2-opt
            full_neighbours = generate_two_opt_neighbours(current_tour)
        else:
            raise ValueError("Unknown neighbourhood type (use 'swap' or '2opt').")

        # === 2. Random subset selection to reduce cost ===
        if neighbourhood == "swap":
            total = len(full_moves)
            k = min(sample_size, total)
            indices = np.random.choice(total, size=k, replace=False)
            candidate_moves = [full_moves[idx] for idx in indices]
        else:  # 2-opt
            total = len(full_neighbours)
            k = min(sample_size, total)
            indices = np.random.choice(total, size=k, replace=False)
            candidate_neighbours = [full_neighbours[idx] for idx in indices]

        # === 3. Evaluate neighbours and select best admissible candidate ===
        best_candidate = None
        best_candidate_cost = float("inf")
        best_move_info = None  # for swap moves

        if neighbourhood == "swap":
            for i, j, cand in candidate_moves:
                cost = tour_length(cand, dist_matrix)

                city_i = current_tour[i]
                city_j = current_tour[j]
                is_tabu = tabu_list[city_i, city_j] > 0 or tabu_list[city_j, city_i] > 0

                # Aspiration: allow tabu if it improves global best
                if is_tabu and cost >= best_cost:
                    continue

                if cost < best_candidate_cost:
                    best_candidate = cand
                    best_candidate_cost = cost
                    best_move_info = (city_i, city_j)

        else:  # 2-opt: no tabu restrictions for simplicity
            for cand in candidate_neighbours:
                cost = tour_length(cand, dist_matrix)
                if cost < best_candidate_cost:
                    best_candidate = cand
                    best_candidate_cost = cost

        # Move to best candidate
        if best_candidate is None:
            # No admissible move found; stop
            break

        current_tour = best_candidate
        current_cost = best_candidate_cost

        # === 4. Update global best & improvement tracking ===
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour.copy()
            last_improvement = iteration

        history.append(best_cost)

        # === 5. Update tabu list (only for swap-based TS) ===
        # Decrease all tabu tenures
        tabu_list = np.maximum(tabu_list - 1, 0)

        if neighbourhood == "swap" and best_move_info is not None:
            city_i, city_j = best_move_info
            tabu_list[city_i, city_j] = tabu_tenure
            tabu_list[city_j, city_i] = tabu_tenure

        # === 6. Adaptive tabu tenure ===
        if iteration > 0 and iteration % adapt_step == 0:
            if (iteration - last_improvement) > adapt_step:
                # No improvement for a while -> increase tenure (more diversification)
                tabu_tenure = min(tenure_max, tabu_tenure + 1)
            else:
                # There has been a recent improvement -> decrease tenure (more intensification)
                tabu_tenure = max(tenure_min, tabu_tenure - 1)

    return best_tour, best_cost, history
