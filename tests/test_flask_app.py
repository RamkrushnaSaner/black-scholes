import sys
from pathlib import Path

# Fix PYTHONPATH for tests
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import json
import pytest

from app.flask_app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
def test_health_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "ok"
    assert "Black-Scholes" in data["service"]
def test_price_endpoint_call_option(client):
    response = client.get(
        "/price",
        query_string={
            "S": 100,
            "X": 100,
            "T": 1,
            "r": 0.05,
            "sigma": 0.2,
            "type": "call",
        },
    )

    assert response.status_code == 200

    data = response.get_json()
    assert "price" in data

    # Known reference value
    assert abs(data["price"] - 10.4506) < 1e-3
def test_price_invalid_option_type(client):
    response = client.get(
        "/price",
        query_string={
            "S": 100,
            "X": 100,
            "T": 1,
            "r": 0.05,
            "sigma": 0.2,
            "type": "invalid",
        },
    )

    assert response.status_code == 400
def test_greeks_endpoint(client):
    response = client.get(
        "/greeks",
        query_string={
            "S": 100,
            "X": 100,
            "T": 1,
            "r": 0.05,
            "sigma": 0.2,
            "type": "call",
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    for greek in ["delta", "gamma", "theta", "vega", "rho"]:
        assert greek in data
        assert isinstance(data[greek], float)
def test_greeks_invalid_type(client):
    response = client.get(
        "/greeks",
        query_string={
            "S": 100,
            "X": 100,
            "T": 1,
            "r": 0.05,
            "sigma": 0.2,
            "type": "invalid",
        },
    )

    assert response.status_code == 400
