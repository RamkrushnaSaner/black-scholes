import numpy as np
import pandas as pd

def compute_annualized_volatility(csv_path, price_column="close"):
    df = pd.read_csv(csv_path)
    returns = df[price_column].pct_change().dropna()
    return np.sqrt(252) * returns.std()
