import numpy as np
from typing import List, Tuple


def swap_cities(tour: np.ndarray, i: int, j: int) -> np.ndarray:
    """
    Swap two cities in a tour and return a new tour.
    """
    new_tour = tour.copy()
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def generate_all_swap_neighbours(tour: np.ndarray) -> List[np.ndarray]:
    """
    Generate all neighbours by swapping every pair of cities.
    """
    neighbours = []
    n = len(tour)

    for i in range(n - 1):
        for j in range(i + 1, n):
            neighbour = swap_cities(tour, i, j)
            neighbours.append(neighbour)

    return neighbours

def generate_random_swap_neighbour(tour: np.ndarray) -> np.ndarray:
    """
    Generate a random neighbouring tour by applying one random swap.
    """
    n = len(tour)
    i, j = np.random.choice(n, size=2, replace=False)
    return swap_cities(tour, i, j)

def generate_all_swap_moves(tour: np.ndarray) -> List[Tuple[int, int, np.ndarray]]:
    """
    Generate all swap neighbours BUT also return the (i, j) indices
    that were swapped. Useful for Tabu Search.

    Returns a list of (i, j, neighbour_tour).
    """
    n = len(tour)
    moves = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            new_tour = tour.copy()
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            moves.append((i, j, new_tour))

    return moves
