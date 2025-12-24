import numpy as np
import matplotlib.pyplot as plt
from src.bs_model import black_scholes

def plot_stock_vs_option(spot_prices, strike, T, r, sigma, option_type="put"):
    option_prices = np.zeros(len(spot_prices))

    for i, S in enumerate(spot_prices):
        option_prices[i] = black_scholes(S, strike, T, r, sigma, option_type)

    fig, ax1 = plt.subplots()
    ax1.plot(spot_prices.index, spot_prices, label="Stock Price", color="blue")
    ax1.set_ylabel("Stock Price")

    ax2 = ax1.twinx()
    ax2.plot(spot_prices.index, option_prices, label="Option Price", color="red")
    ax2.set_ylabel("Option Price")

    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    plt.title("Stock Price vs Option Price")
    plt.show()
