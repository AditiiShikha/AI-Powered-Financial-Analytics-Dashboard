import pandas as pd

def load_data(filepath):
    """
    Load the Sample Superstore dataset.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    try:
        df = pd.read_csv(filepath, encoding="latin1")
        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        raise