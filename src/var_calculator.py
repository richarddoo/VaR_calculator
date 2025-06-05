import numpy as np

def calculate_var_single(pnl_history, confidence_level=0.95):
    """
    Calculate the historcal VaR for a single trade.

    Args:
        pnl_history (list): Historical profit and loss data (losses as negatives).
        confidence_level (float): Confidence level for VaR calculation (0 < confidence_level < 1).

    Returns:
        float: The Value at Risk (VaR) at the specified confidence level (a VaR of 0 means that there is no risk of any losses).
    """
    if not 0 < confidence_level < 1:
        raise ValueError("Confidence level must be between 0 and 1.")
    
    n = len(pnl_history)
    if n == 0:
        raise ValueError("PnL history cannot be empty.")
    
    pnl_sorted = np.sort(pnl_history)
    i = np.floor(n * (1 - confidence_level))
    var = pnl_sorted[int(i)]
    return abs(var) if var <= 0.0 else 0.0

def calculate_var_portfolio(pnl_matrix, confidence_level=0.95):
    """
    Calculate the historical VaR for a portfolio of trades.

    Args:
        pnl_history (list of lists): Historical profit and loss data for multiple trades, shape (n_trades, n_period).
        confidence_level (float): Confidence level for VaR calculation (0 < confidence_level < 1).

    Returns:
        float: The Value at Risk (VaR) at the specified confidence level.
    """
    if not 0 < confidence_level < 1:
        raise ValueError("Confidence level must be between 0 and 1.")
    
    n = len(pnl_matrix)
    if n == 0:
        raise ValueError("PnL history cannot be empty.")

    if np.array(pnl_matrix).ndim != 2:
        raise ValueError("PnL history must be a 2D array (n_periods, n_trades).")
    
    if not all(len(row) == len(pnl_matrix[0]) for row in pnl_matrix):
        raise ValueError("All rows in PnL history must have the same number of trades.")

    if np.array(pnl_matrix).shape[0] == 0 or np.array(pnl_matrix).shape[1] == 0:
        raise ValueError("PnL history cannot have zero periods or trades.")
    
    portfolio_pnl = np.sum(pnl_matrix, axis=0)
    return calculate_var_single(portfolio_pnl, confidence_level)
