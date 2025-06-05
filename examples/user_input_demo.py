from src import calculate_var_single

if __name__ == "__main__":
    # Get PnL history from user
    pnl_input = input("Enter PnL history as comma-separated values (e.g., -100, -50, 10, 20): ")
    try:
        pnl_history = [float(x.strip()) for x in pnl_input.split(',') if x.strip() != '']
    except ValueError:
        print("Invalid PnL input. Please enter only numbers separated by commas.")
        exit()
    
    # Get confidence level from user (optional)
    confidence_input = input("Enter confidence level (e.g., 0.95) or press Enter to use default 0.95: ")
    try:
        confidence_level = float(confidence_input) if confidence_input.strip() else 0.95
    except ValueError:
        print("Invalid confidence level. Please enter a decimal between 0 and 1.")
        exit()

    try:
        var = calculate_var_single(pnl_history, confidence_level)
        print(f"\nValue at Risk (VaR) at {confidence_level*100:.1f}% confidence level: ${var:.2f}")
    except Exception as e:
        print(f"Error: {e}")

