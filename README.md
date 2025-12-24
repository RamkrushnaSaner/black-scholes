![Tests](https://github.com/RamkrushnaSaner/BLACK-SCHOLES/actions/workflows/tests.yml/badge.svg)
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
- Validated with **automated tests (pytest)** and **CI**
- Modular, reusable, and GitHub-ready codebase

---

## 📁 Project Structure

src/ → core Black–Scholes logic
tests/ → automated validation (pytest)
app/ → Tkinter GUI
examples/ → exploratory usage (playground)
data/ → sample market data


🧪 Testing

Automated tests validate pricing accuracy and Greeks behavior against
known Black–Scholes benchmarks.

Run all tests:

pytest


Expected output:

================ 9 passed =================