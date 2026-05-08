import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Charge un fichier CSV en DataFrame."""
    return pd.read_csv(path)

