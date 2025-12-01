import numpy as np
from typing import Sequence

def create_initial_tour(num_cities: int, method: str = "random"):
    if method == "random":
        tour = np.random.permutation(num_cities)
    elif method == "distance":
        tour = np.arange(num_cities)
    else:
        raise ValueError("Invalid method")

    return tour

def tour_length(tour: Sequence[int], distance_matrix: np.ndarray) -> float:
    total_distance = 0.0
    number_of_cities = len(tour)

    for i in range(number_of_cities):
        current_city = tour[i]
        next_city = tour[(i + 1) % number_of_cities]
        total_distance += distance_matrix[current_city, next_city]

    return total_distance

def is_valid_tour(tour: Sequence[int], number_of_cities: int) -> bool:
    tour_array = np.array(tour)

    return(
        len(tour_array) == number_of_cities
        and np.array_equal(np.sort(tour_array), np.arange(number_of_cities))
    )