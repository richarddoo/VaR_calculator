from src import calculate_var_portfolio
import numpy as np

if __name__ == "__main__":
    # Multiple trades, shape: (n_periods, n_trades)
    portfolio_pnl = np.array([
        [-1000, 200],
        [500, 400],
        [-2500, -400],
        [2000, 300],
        [-500, 0],
        [1000, -450],
        [-3000, 500],
        [500, 600],
        [-400, -1000],
        [2700, 0]
    ])
    port_var_95 = calculate_var_portfolio(portfolio_pnl, confidence_level=0.95)
    print(f"Portfolio VaR (95% confidence): ${port_var_95:.2f}")