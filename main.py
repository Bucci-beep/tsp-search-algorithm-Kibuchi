from src.utils import load_cities, create_distance_matrix
from algorithms.tsp_core import create_initial_tour, tour_length, is_valid_tour
from algorithms.neighbourhood import generate_all_swap_neighbours, generate_random_swap_neighbour


def main():
    # Load dataset
    cities_path = "data/cities.csv"
    cities_df = load_cities(cities_path)

    # Display initial dataset summary
    print("Loaded:", cities_df.shape)
    print(cities_df.head())

    # create distance matrix
    dist_matrix = create_distance_matrix(cities_df)
    print("Distance matrix shape:", dist_matrix.shape)

    #create an initial tour
    number_of_cities = len(cities_df)
    initial_tour = create_initial_tour(number_of_cities, method="random")

    print(initial_tour)

    # validate the tour
    valid = is_valid_tour(initial_tour, number_of_cities)
    print(f"\nIs the tour valid? {valid}")

    # compute tour length
    initial_cost = tour_length(initial_tour, dist_matrix)
    print(f"Initial tour length: {initial_cost:.4f}")

    # generate neighbourhood (first 10 neighbours only for preview)
    neighbours = generate_all_swap_neighbours(initial_tour)
    print(f"\nGenerated {len(neighbours)} neighbours via swap operator.")

    print("\nExample neighbours (first 3):")
    for nb in neighbours[:3]:
        print(nb)


if __name__ == "__main__":
    main()
