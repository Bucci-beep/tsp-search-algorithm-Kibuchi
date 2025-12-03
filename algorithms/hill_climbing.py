import numpy as np
from typing import Tuple, List
from algorithms.neighbourhood import generate_all_swap_neighbours
from algorithms.tsp_core import tour_length


def simple_hill_climbing(
    initial_tour: np.ndarray,
    dist_matrix: np.ndarray,
    max_iterations: int = 500
) -> Tuple[np.ndarray, float, List[float]]:
    """
    Perform simple hill climbing to minimise TSP tour length.

    Parameters
    ----------
    initial_tour : np.ndarray
        Starting tour (permutation of city indices).

    dist_matrix : np.ndarray
        Precomputed distance matrix.

    max_iterations : int
        Maximum number of hill climbing iterations.

    Returns
    -------
    best_tour : np.ndarray
        Best tour found.

    best_cost : float
        Cost (length) of the best tour.

    history : List[float]
        Cost at each iteration (for visualisation/debugging).
    """

    current_tour = initial_tour.copy()
    current_cost = tour_length(current_tour, dist_matrix)
    history = [current_cost]

    for iteration in range(max_iterations):

        # Generate all neighbours via swap
        neighbours = generate_all_swap_neighbours(current_tour)[:200]

        # Evaluate neighbours — find the best one
        best_nb = None
        best_nb_cost = float("inf")

        for nb in neighbours:
            cost = tour_length(nb, dist_matrix)
            if cost < best_nb_cost:
                best_nb = nb
                best_nb_cost = cost

        # If the best neighbour is better than current — move
        if best_nb_cost < current_cost:
            current_tour = best_nb
            current_cost = best_nb_cost
            history.append(current_cost)
        else:
            # No improvement → local optimum reached
            break

    return current_tour, current_cost, history
