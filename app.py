from flask import Flask, request
from math import gcd

app = Flask(__name__)

def is_non_negative_integer(value: str):
    if value is None:
        return False
    return value.isdigit()

@app.get("/tapenovs_gmail_com")
def lcm_endpoint():
    x = request.args.get("x")
    y = request.args.get("y")

    if not is_non_negative_integer(x) or not is_non_negative_integer(y):
        return "NaN", 200, {"Content-Type": "text/plain; charset=utf-8"}

    x = int(x)
    y = int(y)

    if x == 0 or y == 0:
        return "0", 200, {"Content-Type": "text/plain; charset=utf-8"}

    result = (x // gcd(x, y)) * y
    return str(result), 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
