import numpy as np

from src.bs_model import (
    black_scholes,
    bs_delta,
    bs_gamma,
    bs_theta,
    bs_vega,
    bs_rho,
    prob
)

# ===============================
# Black–Scholes Price Tests
# ===============================

def test_call_price_known_value():
    """
    Known benchmark:
    S=100, X=100, T=1, r=0.05, sigma=0.2
    Call ≈ 10.45
    """
    price = black_scholes(100, 100, 1, 0.05, 0.2, "call")
    assert np.isclose(price, 10.45, atol=0.05)


def test_put_price_known_value():
    """
    Known benchmark:
    Put ≈ 5.57
    """
    price = black_scholes(100, 100, 1, 0.05, 0.2, "put")
    assert np.isclose(price, 5.57, atol=0.05)


# ===============================
# Greeks – Sanity & Sign Tests
# ===============================

def test_call_delta_range():
    delta = bs_delta(100, 100, 1, 0.05, 0.2, "call")
    assert 0 < delta < 1


def test_put_delta_range():
    delta = bs_delta(100, 100, 1, 0.05, 0.2, "put")
    assert -1 < delta < 0


def test_gamma_positive():
    gamma = bs_gamma(100, 100, 1, 0.05, 0.2)
    assert gamma > 0


def test_vega_positive():
    vega = bs_vega(100, 100, 1, 0.05, 0.2)
    assert vega > 0


def test_theta_negative_for_call():
    theta = bs_theta(100, 100, 1, 0.05, 0.2, "call")
    assert theta < 0


def test_rho_signs():
    rho_call = bs_rho(100, 100, 1, 0.05, 0.2, "call")
    rho_put = bs_rho(100, 100, 1, 0.05, 0.2, "put")

    assert rho_call > 0
    assert rho_put < 0


# ===============================
# Risk-Neutral Probability Tests
# ===============================

def test_probability_bounds():
    p_call = prob(100, 100, 1, 0.05, 0.2, "call")
    p_put = prob(100, 100, 1, 0.05, 0.2, "put")

    assert 0 <= p_call <= 1
    assert 0 <= p_put <= 1
