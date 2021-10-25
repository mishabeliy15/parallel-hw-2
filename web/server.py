#!/usr/bin/env python3
import time

from flask import Flask, request
from factorization import eratosthenes, factorize

app = Flask(__name__)


@app.route("/")
def health_check():
    return "OK"


@app.route("/")
def highload_probe():
    diff = int(request.args.get("time", "1"))
    x = 17
    start = time.time()
    b = True
    while b:
        x * x
        end = time.time()
        if end - start > diff:
            b = False
    return "High load probe done"


@app.route("/factorize")
def factorize_get():
    n = int(request.args.get("n", "100"))
    x = int(request.args.get("x", "10"))
    numbers = eratosthenes(n)
    fact = factorize(x, numbers)
    return {"eratosthenes__len__": len(numbers), "fact": fact}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
