# Black–Scholes Option Pricing Model (Python)

A clean, production-style Python implementation of the **Black–Scholes model** for European options, including Greeks, volatility estimation from market data, visualization, GUI support, and automated testing.

This project focuses on **quantitative finance correctness**.

---

## 🚀 Features

- European **call and put option pricing**
- Full set of **Greeks**: Delta, Gamma, Theta, Vega, Rho
- **Risk-neutral probability** of option exercise
- **Annualized volatility estimation** from historical market data
- **Matplotlib visualization** of stock price vs option value
- **Tkinter GUI** for interactive option pricing
- **Automated testing** with `pytest`
- Modular, reusable, and GitHub-ready codebase

---

## 📁 Project Structure

BLACK-SCHOLES/
│
├── src/ # Core pricing logic
│ ├── bs_model.py # Black–Scholes formula + Greeks
│ ├── volatility.py # Volatility estimation
│ └── visualization.py # Plotting utilities
│
├── app/ # User interfaces
│ └── tkinter_app.py # GUI application
│
├── tests/ # Automated tests
│ └── test_bs_model.py
│
├── data/ # Market data
│ └── IBM_returns.csv
│
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── LICENSE
└── .gitignore

▶️ Usage
Price an option programmatically
from src.bs_model import black_scholes
Example:
price = black_scholes(
    S=70,
    X=80,
    T=0.5,
    r=0.02,
    sigma=0.3,
    option_type="call"
)

print(price)


Run the GUI
python -m app.tkinter_app


Compute volatility from market data
from src.volatility import compute_annualized_volatility
sigma = compute_annualized_volatility("data/IBM_returns.csv")


Visualize stock price vs option value
from src.visualization import plot_stock_vs_option
Example:
plot_stock_vs_option(
    spot_prices,
    strike=140,
    T=0.5,
    r=0.02,
    sigma=sigma,
    option_type="put"
)

🧪 Testing

Automated tests validate pricing accuracy and Greeks behavior against
known Black–Scholes benchmarks.

Run all tests:

pytest


Expected output:

================ 9 passed =================