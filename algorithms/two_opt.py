import numpy as np

def two_opt_swap(tour: np.ndarray, i: int, k: int) -> np.ndarray:
    """
    Performs a 2-opt swap: reverse the segment tour[i:k+1].
    """
    new_tour = tour.copy()
    new_tour[i:k+1] = new_tour[i:k+1][::-1]
    return new_tour


def generate_two_opt_neighbours(tour):
    """
        Generate all neighbours using the 2-opt swap operator.

        Parameters
        ----------
        tour : np.ndarray

        Returns
        -------
        List of new tours generated using 2-opt swaps.
        """
    neighbours = []
    n = len(tour)

    for i in range(n - 1):
        for k in range(i + 1, n):
            neighbour = two_opt_swap(tour, i, k)
            neighbours.append(neighbour)

    return neighbours
