from src.bs_model import (
    black_scholes, bs_delta, bs_gamma, bs_theta, bs_vega, bs_rho, prob
)
import tkinter as tk
from tkinter import ttk

def calculate():
    S = float(entry_S.get())
    X = float(entry_X.get())
    T = float(entry_T.get())
    r = float(entry_r.get())
    sigma = float(entry_sigma.get())
    option_type = option_type_var.get()

    value = black_scholes(S, X, T, r, sigma, option_type)
    delta = bs_delta(S, X, T, r, sigma, option_type)

    result_label.config(text=f"Option Value: {value:.4f}\nDelta: {delta:.4f}")

root = tk.Tk()
root.title("Black-Scholes Calculator")

labels = ["S", "X", "T", "r", "sigma"]
entries = []

for i, lbl in enumerate(labels):
    ttk.Label(root, text=lbl).grid(row=i, column=0)
    entry = ttk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

entry_S, entry_X, entry_T, entry_r, entry_sigma = entries

option_type_var = tk.StringVar(value="call")
ttk.Combobox(root, values=["call", "put"], textvariable=option_type_var).grid(row=5, column=1)

ttk.Button(root, text="Calculate", command=calculate).grid(row=6, column=0, columnspan=2)
result_label = ttk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
