#!/usr/bin/env python3
"""the app Module"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', method=["GET"], strict_slashes=False)
def index() -> str:
    """employs the get mthod at root"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    """main to test"""
    app.run(host="0.0.0.0", port="5000")
