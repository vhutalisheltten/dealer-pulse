import os

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


def evaluate_dealer(payload):
    required = ("name", "sales", "satisfaction", "response_time")
    missing = [field for field in required if payload.get(field) in (None, "")]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    name = str(payload["name"]).strip()
    sales = max(0, float(payload["sales"]))
    satisfaction = min(5, max(0, float(payload["satisfaction"])))
    response_time = max(0, float(payload["response_time"]))

    sales_score = min(sales / 100, 1) * 40
    satisfaction_score = satisfaction / 5 * 45
    response_score = max(0, 1 - response_time / 72) * 15
    score = round(sales_score + satisfaction_score + response_score, 1)

    if score >= 85:
        rating = "Exceptional"
    elif score >= 70:
        rating = "Strong"
    elif score >= 55:
        rating = "Developing"
    else:
        rating = "Needs attention"

    return {
        "name": name,
        "score": score,
        "rating": rating,
        "metrics": {
            "monthly_sales": sales,
            "customer_satisfaction": satisfaction,
            "response_time_hours": response_time,
        },
    }


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/api/evaluate")
def evaluate():
    try:
        return jsonify(evaluate_dealer(request.get_json(silent=True) or {}))
    except (TypeError, ValueError) as exc:
        return jsonify(error=str(exc)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
