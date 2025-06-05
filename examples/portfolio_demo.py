from src import calculate_var_portfolio

if __name__ == "__main__":
    # Multiple trades, shape: (n_trades, n_periods)
    portfolio_pnl = [[-1000, 500, -2500, 2000, -500, 1000, -3000, 500, -400, 2700],
                     [-200, 400, -400, 300, 0, -450, 500, 600, -1000, 0]]
    print("Portfolio PnL data:")
    for i, trade in enumerate(portfolio_pnl):
        print(f"Trade {i+1}: {trade}")

    port_var_95 = calculate_var_portfolio(portfolio_pnl, confidence_level=0.95)
    print(f"\nPortfolio VaR (95% confidence): ${port_var_95:.2f}")