import numpy as np
from scipy.stats import norm

def d11(S, X, T, r, sigma):
    return (np.log(S / X) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d21(d1, T, sigma):
    return d1 - sigma * np.sqrt(T)

def black_scholes(S, X, T, r, sigma, option_type):
    d1 = d11(S, X, T, r, sigma)
    d2 = d21(d1, T, sigma)

    if option_type == "call":
        return S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def bs_delta(S, X, T, r, sigma, option_type):
    if option_type == "call":
        return norm.cdf(d11(S, X, T, r, sigma))
    elif option_type == "put":
        return norm.cdf(d11(S, X, T, r, sigma)) - 1
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def bs_gamma(S, X, T, r, sigma):
    d1 = d11(S, X, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def bs_theta(S, X, T, r, sigma, option_type):
    d1 = d11(S, X, T, r, sigma)
    d2 = d21(d1, T, sigma)
    first_term = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    if option_type == "call":
        return first_term - r * X * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return first_term + r * X * np.exp(-r * T) * norm.cdf(-d2)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def bs_vega(S, X, T, r, sigma):
    return S * norm.pdf(d11(S, X, T, r, sigma)) * np.sqrt(T)

def bs_rho(S, X, T, r, sigma, option_type):
    d2 = d21(d11(S, X, T, r, sigma), T, sigma)

    if option_type == "call":
        return X * T * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return -X * T * np.exp(-r * T) * norm.cdf(-d2)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def prob(S, X, T, r, sigma, option_type):
    d2 = d21(d11(S, X, T, r, sigma), T, sigma)

    if option_type == "call":
        return norm.cdf(d2)
    elif option_type == "put":
        return norm.cdf(-d2)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
