"""
playground.py

Exploratory script to manually test and understand the behavior
of the Black–Scholes pricing model. Not part of automated tests.
"""


from src.bs_model import black_scholes, bs_delta, prob
from src.volatility import compute_annualized_volatility
import numpy as np

print("=== ATM Call Option ===")
print(black_scholes(100, 100, 1, 0.05, 0.2, "call"))

print("\n=== Deep ITM Call ===")
print(black_scholes(150, 100, 1, 0.05, 0.2, "call"))
print("Delta:", bs_delta(150, 100, 1, 0.05, 0.2, "call"))

print("\n=== Deep OTM Call ===")
print(black_scholes(50, 100, 1, 0.05, 0.2, "call"))

print("\n=== Volatility Sensitivity ===")
print("Low vol:", black_scholes(100, 100, 1, 0.05, 0.1, "call"))
print("High vol:", black_scholes(100, 100, 1, 0.05, 0.4, "call"))

print("\n=== Call-Put Parity ===")
S, X, T, r, sigma = 100, 100, 1, 0.05, 0.2
call = black_scholes(S, X, T, r, sigma, "call")
put = black_scholes(S, X, T, r, sigma, "put")
print("C - P:", call - put)
print("S - Xe^{-rT}:", S - X * np.exp(-r * T))

print("\n=== IBM Market Example ===")
sigma_ibm = compute_annualized_volatility("data/IBM_returns.csv")
print("IBM sigma:", sigma_ibm)
print(
    black_scholes(140, 150, 0.5, 0.02, sigma_ibm, "put")
)
