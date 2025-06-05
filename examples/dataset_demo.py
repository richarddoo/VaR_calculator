from src import calculate_var_portfolio
import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    df_path = Path('data/sample_data.csv')
    df = pd.read_csv(df_path)
    df = df.drop(columns=["Date"])

    portfolio_pnl = df.T.values.tolist()

    port_var_95 = calculate_var_portfolio(portfolio_pnl, confidence_level=0.95)
    print(f"\nPortfolio VaR (95% confidence): ${port_var_95:.2f}")