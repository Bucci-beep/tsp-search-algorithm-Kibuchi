import pandas as pd

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
