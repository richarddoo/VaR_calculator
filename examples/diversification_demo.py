from src import calculate_var_portfolio
from src import calculate_var_single

if __name__ == "__main__":
    portfolio_pnl = [[320, -110, 50, -80, -250, -430, -200, 130, 250, 90],
                     [410, -70, -200, -250, 350, 120, -480, 20, -360, 100]]
    print("Portfolio PnL data:")
    for i, trade in enumerate(portfolio_pnl):
        print(f"Trade {i+1}: {trade}")
    
    # Portfolio VaR
    port_var_95 = calculate_var_portfolio(portfolio_pnl, confidence_level=0.95)
    print(f"\nPortfolio VaR (95% confidence): ${port_var_95:.2f}\n")

    # Individual VaRs
    var1 = calculate_var_single(portfolio_pnl[0], confidence_level=0.95)
    var2 = calculate_var_single(portfolio_pnl[1], confidence_level=0.95)
    print(f"Trade 1 VaR (95% confidence): ${var1:.2f}")
    print(f"Trade 2 VaR (95% confidence): ${var2:.2f}")
    sum_vars = var1 + var2
    print(f"Sum of individual VaRs: ${sum_vars:.2f}")

    print(f"\nDiversification benefit: ${sum_vars - port_var_95:.2f}") 