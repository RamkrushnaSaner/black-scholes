"""
Black–Scholes Quant App (Streamlit)

Frontend UI that consumes a Flask backend API
for Black–Scholes pricing and Greeks.
"""

# ===============================
# Imports
# ===============================
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import requests

# ===============================
# Backend configuration
# ===============================
FLASK_API_URL = "http://127.0.0.1:5000"

# ===============================
# API helper functions
# ===============================
def fetch_price(S, X, T, r, sigma, option_type):
    response = requests.get(
        f"{FLASK_API_URL}/price",
        params={
            "S": S,
            "X": X,
            "T": T,
            "r": r,
            "sigma": sigma,
            "type": option_type,
        },
        timeout=5,
    )
    response.raise_for_status()
    return response.json()["price"]


def fetch_greeks(S, X, T, r, sigma, option_type):
    response = requests.get(
        f"{FLASK_API_URL}/greeks",
        params={
            "S": S,
            "X": X,
            "T": T,
            "r": r,
            "sigma": sigma,
            "type": option_type,
        },
        timeout=5,
    )
    response.raise_for_status()
    return response.json()

# ===============================
# Page configuration
# ===============================
st.set_page_config(
    page_title="Black–Scholes | Quant Pricing",
    layout="wide",
)

# ===============================
# Header
# ===============================
st.title("📐 Black–Scholes Option Pricing")
st.caption(
    "Frontend UI consuming a Flask API for European option pricing and risk analytics"
)

st.divider()

# ===============================
# Sidebar – Model Inputs
# ===============================
st.sidebar.header("Model Parameters")

S = st.sidebar.number_input("Spot Price (S)", value=100.0, min_value=0.01)
X = st.sidebar.number_input("Strike Price (X)", value=100.0, min_value=0.01)
T = st.sidebar.number_input("Time to Maturity (T, years)", value=1.0, min_value=0.01)
r = st.sidebar.number_input("Risk-free Rate (r)", value=0.05, format="%.4f")
sigma = st.sidebar.number_input("Volatility (σ)", value=0.2, min_value=0.01)

option_type = st.sidebar.selectbox("Option Type", ["call", "put"])

st.sidebar.divider()

# ===============================
# Sensitivity Controls
# ===============================
st.sidebar.subheader("Sensitivity Range (Spot Price)")

S_min = st.sidebar.number_input("Min Spot", value=max(0.01, S * 0.5))
S_max = st.sidebar.number_input("Max Spot", value=S * 1.5)

# ===============================
# Pricing & Greeks (API Call)
# ===============================
try:
    price = fetch_price(S, X, T, r, sigma, option_type)
    greeks = fetch_greeks(S, X, T, r, sigma, option_type)

    delta = greeks["delta"]
    gamma = greeks["gamma"]
    theta = greeks["theta"]
    vega = greeks["vega"]
    rho = greeks["rho"]

except Exception as e:
    st.error(f"Backend error: {e}")
    st.stop()

# ===============================
# Layout
# ===============================
col_left, col_right = st.columns([1.1, 1])

# -------------------------------
# Mathematical Formulation
# -------------------------------
with col_left:
    st.subheader("📘 Mathematical Model")

    st.latex(
        r"""
        d_1 = \frac{\ln(S/X) + (r + \frac{1}{2}\sigma^2)T}{\sigma \sqrt{T}},
        \qquad
        d_2 = d_1 - \sigma \sqrt{T}
        """
    )

    if option_type == "call":
        st.latex(r"C = S N(d_1) - X e^{-rT} N(d_2)")
    else:
        st.latex(r"P = X e^{-rT} N(-d_2) - S N(-d_1)")

    st.markdown(
        """
        **Model Assumptions**
        - Log-normal asset prices  
        - Constant volatility  
        - No arbitrage  
        - Frictionless markets  
        - European exercise  
        """
    )

# -------------------------------
# Pricing Output
# -------------------------------
with col_right:
    st.subheader("📊 Pricing & Greeks")

    st.metric("Option Price", f"{price:.4f}")

    g1, g2, g3 = st.columns(3)
    g1.metric("Delta (Δ)", f"{delta:.4f}")
    g2.metric("Gamma (Γ)", f"{gamma:.6f}")
    g3.metric("Theta (Θ)", f"{theta:.4f}")

    g4, g5 = st.columns(2)
    g4.metric("Vega (ν)", f"{vega:.4f}")
    g5.metric("Rho (ρ)", f"{rho:.4f}")

# ===============================
# Sensitivity Analysis (via API)
# ===============================
st.divider()
st.subheader("📉 Greeks Sensitivity vs Spot Price")

S_range = np.linspace(S_min, S_max, 100)

delta_vals = []
gamma_vals = []
theta_vals = []
vega_vals = []
rho_vals = []

for s in S_range:
    g = fetch_greeks(s, X, T, r, sigma, option_type)
    delta_vals.append(g["delta"])
    gamma_vals.append(g["gamma"])
    theta_vals.append(g["theta"])
    vega_vals.append(g["vega"])
    rho_vals.append(g["rho"])

fig, ax = plt.subplots(3, 2, figsize=(11, 10))
fig.tight_layout(pad=4)

ax[0, 0].plot(S_range, delta_vals); ax[0, 0].set_title("Delta (Δ)")
ax[0, 1].plot(S_range, gamma_vals); ax[0, 1].set_title("Gamma (Γ)")
ax[1, 0].plot(S_range, theta_vals); ax[1, 0].set_title("Theta (Θ)")
ax[1, 1].plot(S_range, vega_vals);  ax[1, 1].set_title("Vega (ν)")
ax[2, 0].plot(S_range, rho_vals);   ax[2, 0].set_title("Rho (ρ)")
ax[2, 1].axis("off")

for row in ax:
    for a in row:
        a.grid(True)

st.pyplot(fig)

# ===============================
# Footer
# ===============================
st.divider()
st.caption(
    "Streamlit frontend consuming a Flask backend API. "
    "All values computed under the risk-neutral measure."
)
