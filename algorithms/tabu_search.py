import numpy as np
from typing import Tuple, List
from algorithms.neighbourhood import swap_cities, generate_all_swap_neighbours
from algorithms.tsp_core import tour_length


def tabu_search(
    initial_tour: np.ndarray,
    dist_matrix: np.ndarray,
    tabu_tenure: int = 10,
    max_iterations: int = 200,
) -> Tuple[np.ndarray, float, List[float]]:
    """
    Tabu Search algorithm for the TSP using swap-based neighbourhoods.

    Parameters
    ----------
    initial_tour : np.ndarray
        Starting solution (permutation of city indices).

    dist_matrix : np.ndarray
        Precomputed distance matrix.

    tabu_tenure : int
        Number of iterations a move remains tabu.

    max_iterations : int
        Maximum number of iterations.

    Returns
    -------
    best_tour : np.ndarray
        Best tour found during the search.

    best_cost : float
        Cost of the best tour.

    history : List[float]
        Cost of the best solution at each iteration.
    """

    n = len(initial_tour)
    current_tour = initial_tour.copy()
    current_cost = tour_length(current_tour, dist_matrix)

    best_tour = current_tour.copy()
    best_cost = current_cost

    # History for analysis / plotting
    history = [best_cost]

    # Tabu list stored as a matrix of tabu tenures for swaps
    tabu_list = np.zeros((n, n), dtype=int)

    for iteration in range(max_iterations):

        best_candidate = None
        best_candidate_cost = float("inf")
        best_move = None

        # Explore all swap neighbours
        for i in range(n - 1):
            for j in range(i + 1, n):

                candidate = swap_cities(current_tour, i, j)
                cost = tour_length(candidate, dist_matrix)

                # Aspiration criterion:
                # allow tabu move if it improves the global best
                is_tabu = tabu_list[i, j] > 0
                if is_tabu and cost >= best_cost:
                    continue

                # Otherwise: accept best non-tabu move
                if cost < best_candidate_cost:
                    best_candidate = candidate
                    best_candidate_cost = cost
                    best_move = (i, j)

        # Move to best candidate
        current_tour = best_candidate
        current_cost = best_candidate_cost

        # Decrease all tabu tenures
        tabu_list = np.maximum(tabu_list - 1, 0)

        # Add the performed swap to tabu list
        i, j = best_move
        tabu_list[i, j] = tabu_tenure

        # Update global best
        if current_cost < best_cost:
            best_tour = current_tour.copy()
            best_cost = current_cost

        history.append(best_cost)

    return best_tour, best_cost, history
