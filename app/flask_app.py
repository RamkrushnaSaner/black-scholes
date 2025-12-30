import sys
from pathlib import Path

# Fix PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from flask import Flask, request, jsonify

from src.bs_model import (
    black_scholes,
    bs_delta,
    bs_gamma,
    bs_theta,
    bs_vega,
    bs_rho,
)

app = Flask(__name__)


@app.route("/")
def health():
    return jsonify({"status": "ok", "service": "Black-Scholes API"})


@app.route("/price", methods=["GET"])
def price_option():
    try:
        S = float(request.args.get("S"))
        X = float(request.args.get("X"))
        T = float(request.args.get("T"))
        r = float(request.args.get("r"))
        sigma = float(request.args.get("sigma"))
        option_type = request.args.get("type")

        if option_type not in {"call", "put"}:
            return jsonify({"error": "option type must be 'call' or 'put'"}), 400

        price = black_scholes(S, X, T, r, sigma, option_type)

        return jsonify({
            "price": round(price, 6),
            "inputs": {
                "S": S,
                "X": X,
                "T": T,
                "r": r,
                "sigma": sigma,
                "type": option_type,
            },
        })

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input parameters"}), 400


@app.route("/greeks", methods=["GET"])
def greeks():
    try:
        S = float(request.args.get("S"))
        X = float(request.args.get("X"))
        T = float(request.args.get("T"))
        r = float(request.args.get("r"))
        sigma = float(request.args.get("sigma"))
        option_type = request.args.get("type")

        if option_type not in {"call", "put"}:
            return jsonify({"error": "Invalid option type"}), 400

        return jsonify({
            "delta": bs_delta(S, X, T, r, sigma, option_type),
            "gamma": bs_gamma(S, X, T, r, sigma),
            "theta": bs_theta(S, X, T, r, sigma, option_type),
            "vega": bs_vega(S, X, T, r, sigma),
            "rho": bs_rho(S, X, T, r, sigma, option_type),
        })

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input parameters"}), 400


if __name__ == "__main__":
    app.run(debug=True)
