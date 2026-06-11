import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset and display tis dimensions.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except Exception as e:
        print(f"Error: Unable to load file - {type(e).__name__}")
        return None


""" if __name__ == "__main__":
    result = load("life_expectancy_years.csv")
    if result is not None:
        print(result) """
