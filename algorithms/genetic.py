import numpy as np
from typing import Tuple, List
from algorithms.tsp_core import tour_length


def create_initial_population(pop_size: int, num_cities: int) -> np.ndarray:
    """
    Create an initial population of random tours.
    Shape: (pop_size, num_cities)
    """
    population = []
    for _ in range(pop_size):
        tour = np.random.permutation(num_cities)
        population.append(tour)
    return np.array(population)


def evaluate_population(population: np.ndarray, dist_matrix: np.ndarray) -> np.ndarray:
    """
    Compute tour length for each individual in the population.
    """
    return np.array([tour_length(ind, dist_matrix) for ind in population])


def tournament_selection(population: np.ndarray, costs: np.ndarray, k: int = 3) -> np.ndarray:
    """
    Tournament selection: pick k random individuals, return the best.
    """
    indices = np.random.choice(len(population), size=k, replace=False)
    best_idx = indices[np.argmin(costs[indices])]
    return population[best_idx]


def ordered_crossover(parent1: np.ndarray, parent2: np.ndarray) -> np.ndarray:
    """
    Ordered crossover (OX) for permutation-based TSP tours.
    """
    n = len(parent1)
    child = -np.ones(n, dtype=int)

    # Random slice from parent1
    a, b = sorted(np.random.choice(n, size=2, replace=False))
    child[a:b+1] = parent1[a:b+1]

    # Fill remaining positions from parent2 in order
    pos = (b + 1) % n
    for city in parent2:
        if city not in child:
            child[pos] = city
            pos = (pos + 1) % n

    return child


def swap_mutation(tour: np.ndarray, mutation_rate: float = 0.1) -> np.ndarray:
    """
    Swap mutation: with some probability, swap two cities.
    """
    new_tour = tour.copy()
    if np.random.rand() < mutation_rate:
        i, j = np.random.choice(len(tour), size=2, replace=False)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour


def genetic_algorithm(
    dist_matrix: np.ndarray,
    num_cities: int,
    pop_size: int = 60,
    generations: int = 200,
    mutation_rate: float = 0.1,
    tournament_k: int = 3,
) -> Tuple[np.ndarray, float, List[float]]:
    """
    Simple Genetic Algorithm for the TSP using:
    - permutation encoding
    - ordered crossover (OX)
    - swap mutation
    - tournament selection
    """

    # Initialise population
    population = create_initial_population(pop_size, num_cities)
    costs = evaluate_population(population, dist_matrix)

    best_idx = np.argmin(costs)
    best_tour = population[best_idx].copy()
    best_cost = costs[best_idx]

    history = [best_cost]

    for _ in range(generations):
        new_population = []

        for _ in range(pop_size):
            # Selection
            parent1 = tournament_selection(population, costs, k=tournament_k)
            parent2 = tournament_selection(population, costs, k=tournament_k)

            # Crossover
            child = ordered_crossover(parent1, parent2)

            # Mutation
            child = swap_mutation(child, mutation_rate)

            new_population.append(child)

        population = np.array(new_population)
        costs = evaluate_population(population, dist_matrix)

        best_idx = np.argmin(costs)
        if costs[best_idx] < best_cost:
            best_cost = costs[best_idx]
            best_tour = population[best_idx].copy()

        history.append(best_cost)

    return best_tour, best_cost, history
