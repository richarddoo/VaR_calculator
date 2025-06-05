# Value at Risk (VaR) Calculator

A Python application for calculating Value at Risk (VaR) based on historical profit and loss data.

## Features

- Calculate VaR for single trades
- Calculate VaR for portfolios of trades
- Configurable confidence levels

## Installation
### Pre-requisites
- Python 3.6 or higher
- pip

```bash
# Clone repo
git clone https://github.com/richarddoo/VaR_calculator.git
cd VaR_calculator
# Install dependencies
pip install -r requirements.txt
```

## Project Structure

### Source Code (`src/`)
- `var_calculator.py` - Main VaR calculation logic

### Tests (`tests/`)
- `test_var_calculator.py` - Unit tests for the VaR calculator

### Examples (`examples/`)
- `simple_demo.py` - Basic usage example on a single trade
- `portfolio_demo.py` - Usage example on a portfolio
- `user_input_demo.py` - Example prompting the user to provide inputs
- `diversification_demo.py` - Example demonstrating the diversification benefit
- `dataset_demo.py` - Example demonstrating the use of a dataset with the application

### Data (`data/`)
- `sample_data.csv` - Data containing historical profit and loss data for multiple trades

### Project Files
- `README.md` - Project documentation
- `requirements.txt` - Project dependencies

## Usage

```bash
python src/var_calculator.py
```

## Example
```python
from src import calculate_var_single

if __name__ == "__main__":
    # Example historical PnL data for a single trade
    trade_pnl = [-1000, 500, -2500, 2000, -500, 1000, -3000, 500, -400, 2700]
    var_95 = calculate_var_single(trade_pnl, confidence_level=0.95)
    print(f"Single Trade VaR (95% confidence): ${var_95:.2f}")
```

```bash
python -m examples.simple_demo
```

## Running Tests
```bash
python -m pytest tests/
```

## Troubleshooting Issues

### If getting an error when trying to import numpy or pandas
Most likely the versions you have of numpy or pandas are incompatible. 
Uninstall both packages first.
```bash
pip uninstall numpy pandas -y
```

Then re-install the requirements.
```bash
pip install -r requirements.txt
```