from src import calculate_var_single

if __name__ == "__main__":
    # Example historical PnL data for a single trade
    trade_pnl = [-1000, 500, -2500, 2000, -500, 1000, -3000, 500, -400, 2700]
    print("Trade PnL data:")
    for i, pnl in enumerate(trade_pnl):
        print(f"Period {i+1}: ${pnl:.2f}")

    var_95 = calculate_var_single(trade_pnl, confidence_level=0.95)
    print(f"\nSingle Trade VaR (95% confidence): ${var_95:.2f}")

