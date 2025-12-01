from src.utils import load_cities, create_distance_matrix

def main():
    # Load dataset
    cities_path = "data/cities.csv"
    cities_df = load_cities(cities_path)

    # Display initial dataset summary
    print("Loaded:", cities_df.shape)
    print(cities_df.head())

    dist_matrix = create_distance_matrix(cities_df)
    print("Distance matrix shape:", dist_matrix.shape)

    # Preview few distances
    print(dist_matrix[:5, :5])

if __name__ == "__main__":
    main()
