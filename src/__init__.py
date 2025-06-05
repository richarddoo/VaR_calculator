"""
Value at Risk (VaR) Calculator package.

A Python library for calculating Value at Risk (VaR) based on historical profit and loss data.

This package provides functions to calculate VaR for both single trades and portfolios of trades, using historical PnL data.

The method of calculation is based on historical simulation, which involves sorting the historical PnL data and determining the VaR at a specified confidence level.
The final VaR value is returned as a positive number, indicating the maximum expected loss at the specified confidence level.
If the calculated VaR is zero or positive, it is returned as zero, indicating no risk of loss at the specified confidence level.
"""

__version__ = "0.1.0"

from .var_calculator import calculate_var_single, calculate_var_portfolio