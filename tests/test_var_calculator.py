import unittest
import numpy as np
from src import calculate_var_single, calculate_var_portfolio

class TestVarCalculator(unittest.TestCase):

    def test_var_single_95(self):
        pnl = [-1000, 500, -2500, 2000, -500, 1000, -3000, 500, -400, 2700]
        # Sorted PnL: [-3000, -2500, -1400, -1200, -500, 500, 900, 1100, 2000, 2700]
        # The index for the 5th percentile is: floor(10 * (1 - 0.95)) = floor(0.5) = 0
        # So we take the first element in the sorted array, which is -3000
        # VaR = abs(-3000) = 3000.0
        var_95 = calculate_var_single(pnl, confidence_level=0.95)
        self.assertAlmostEqual(var_95, 3000.0, places=2)
    
    def test_var_single_99(self):
        pnl = [-200, -100, 0, 100, 200]
        # Sorted PnL: [-200, -100, 0, 100, 200]
        # The index for the 1st percentile is: floor(5 * (1 - 0.99)) = floor(0.05) = 0
        # So we take the first element in the sorted array, which is -200
        var_99 = calculate_var_single(pnl, confidence_level=0.99)
        self.assertAlmostEqual(var_99, 200.0, places=2)
    
    def test_var_single_default_ci(self):
        pnl = [-100, -50, 10, 20, -30, 40, -80, 60, -10, 5]
        # Default confidence level is 0.95
        # Sorted PnL: [-100, -80, -50, -30, -10, 5, 10, 20, 40, 60]
        # The index for the 5th percentile is: floor(10 * (1 - 0.95)) = floor(0.5) = 0
        # So we take the first element in the sorted array, which is -100
        var_default = calculate_var_single(pnl)
        self.assertAlmostEqual(var_default, 100.0, places=2)
    
    def test_var_single_all_positive_pnl(self):
        pnl = [100, 200, 300, 400, 500]
        # All positive PnL, so VaR should be 0
        var_95 = calculate_var_single(pnl, confidence_level=0.95)
        self.assertAlmostEqual(var_95, 0.0, places=2)

    def test_var_single_empty(self):
        with self.assertRaises(ValueError):
            calculate_var_single([], confidence_level=0.95)

    def test_var_portfolio(self):
        pnl_matrix = [[-1000, 500, -2500, 2000, -500, 1000, -3000, 500, -400, 2700],
                      [-200, 400, -400, 300, 0, -450, 500, 600, -1000, 0]]
        port_var_95 = calculate_var_portfolio(pnl_matrix, confidence_level=0.95)
        # Portfolio PnL (sum per row): [-1200, 900, -2900, 2300, -500, 550, -2500, 1100, -1400, 2700]
        # Sorted: [-2900, -2500, -1400, -1200, -500, 550, 900, 1100, 2300, 2700]
        # The index for the 5th percentile is: floor(10 * (1 - 0.95)) = floor(0.5) = 0
        # So we take the first element in the sorted array, which is -2900
        self.assertAlmostEqual(port_var_95, 2900.0, places=2)

    def test_var_portfolio_different_length_trades(self):
        pnl_matrix = [[-1000, 500, -2500, 2000],
                      [-200, 400, -400, 300, 0],
                      [-300, 600, -1000]]
        with self.assertRaises(ValueError):
            calculate_var_portfolio(pnl_matrix, confidence_level=0.95)

    def test_var_portfolio_empty(self):
        with self.assertRaises(ValueError):
            calculate_var_portfolio([], confidence_level=0.95)

    def test_var_portfolio_invalid_shape(self):
        pnl_matrix = [-1000, 500, -2500, 2000]
        with self.assertRaises(ValueError):
            calculate_var_portfolio(pnl_matrix, confidence_level=0.95)
    
    def test_var_portfolio_zero_trades(self):
        pnl_matrix = [[], []]
        with self.assertRaises(ValueError):
            calculate_var_portfolio(pnl_matrix, confidence_level=0.95)

    def test_invalid_confidence(self):
        with self.assertRaises(ValueError):
            calculate_var_single([1, 2, 3], confidence_level=1.05)
        
        with self.assertRaises(ValueError):
            calculate_var_portfolio([[1, 2], [3, 4]], confidence_level=0)

if __name__ == "__main__":
    unittest.main()