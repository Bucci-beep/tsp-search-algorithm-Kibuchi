from src.utils import load_cities

def main():
    # Load dataset
    cities_path = "data/cities.csv"
    cities_df = load_cities(cities_path)

    # Display initial dataset summary
    print("Cities dataset loaded successfully!")
    print("Shape:", cities_df.shape)
    print("\nPreview:")
    print(cities_df.head())

    print("\nProject setup complete. Ready for algorithm implementation.")


if __name__ == "__main__":
    main()
