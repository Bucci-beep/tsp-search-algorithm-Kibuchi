import numpy as np
from typing import Tuple, List
from algorithms.neighbourhood import generate_all_swap_neighbours
from algorithms.two_opt import generate_two_opt_neighbours
from algorithms.tsp_core import tour_length


def simple_hill_climbing(
    initial_tour: np.ndarray,
    dist_matrix: np.ndarray,
    max_iterations: int = 200,
    neighbourhood: str = "swap",      # <-- NEW PARAMETER
    sample_size: int | None = None    # <-- OPTIONAL SPEED-UP PARAMETER
) -> Tuple[np.ndarray, float, List[float]]:
    """
    Hill Climbing with selectable neighbourhood operator:
    - 'swap'  : simple pairwise swap
    - '2opt'  : 2-opt swap
    """

    current_tour = initial_tour.copy()
    current_cost = tour_length(current_tour, dist_matrix)
    history = [current_cost]

    for iteration in range(max_iterations):

        # Choose neighbourhood operator
        if neighbourhood == "swap":
            neighbours = generate_all_swap_neighbours(current_tour)
        elif neighbourhood == "2opt":
            neighbours = generate_two_opt_neighbours(current_tour)
        else:
            raise ValueError("Unknown neighbourhood type specified.")

        # Optional random subset for speed
        if sample_size is not None and len(neighbours) > sample_size:
            idx = np.random.choice(len(neighbours), size=sample_size, replace=False)
            neighbours = [neighbours[i] for i in idx]

        # Evaluate neighbours
        best_nb = None
        best_nb_cost = float("inf")

        for nb in neighbours:
            cost = tour_length(nb, dist_matrix)
            if cost < best_nb_cost:
                best_nb = nb
                best_nb_cost = cost

        # Move if improvement found
        if best_nb_cost < current_cost:
            current_tour = best_nb
            current_cost = best_nb_cost
            history.append(current_cost)
        else:
            break  # reached local optimum

    return current_tour, current_cost, history
