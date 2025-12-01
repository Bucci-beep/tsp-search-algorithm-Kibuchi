import pandas as pd
import numpy as np

def load_cities(path: str) -> pd.DataFrame:
    """
    Load city coordinates from a CSV file.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the file at: {path}")
    except Exception as e:
        raise Exception(f"Error loading cities: {e}")

# euclidian distance function

def compute_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# full distance matrix

def create_distance_matrix(cities_df):
    n = len(cities_df)
    dist_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            xi, yi = cities_df.iloc[i][['X', 'Y']]
            xj, yj = cities_df.iloc[j][['X', 'Y']]
            dist_matrix[i, j] = compute_distance(xi, yi, xj, yj)

    return dist_matrix
