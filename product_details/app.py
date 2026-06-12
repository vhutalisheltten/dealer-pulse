import os

from flask import Flask, jsonify


app = Flask(__name__)

PRODUCTS = {
    1: {
        "id": 1,
        "name": "Roadster X",
        "category": "Electric",
        "price": 42900,
        "description": "A responsive electric roadster built for everyday driving.",
    },
    2: {
        "id": 2,
        "name": "Summit SUV",
        "category": "Hybrid",
        "price": 51800,
        "description": "A spacious hybrid SUV with confident all-weather capability.",
    },
}


@app.get("/")
def index():
    return jsonify(service="product-details", products=list(PRODUCTS.values()))


@app.get("/products/<int:product_id>")
def product_details(product_id):
    product = PRODUCTS.get(product_id)
    if product is None:
        return jsonify(error="Product not found"), 404
    return jsonify(product)


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
