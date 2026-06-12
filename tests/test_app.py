from app import app, evaluate_dealer


def test_evaluate_dealer():
    result = evaluate_dealer(
        {"name": "Northstar", "sales": 100, "satisfaction": 5, "response_time": 0}
    )
    assert result["score"] == 100
    assert result["rating"] == "Exceptional"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_evaluate_rejects_missing_fields():
    client = app.test_client()
    response = client.post("/api/evaluate", json={"name": "Incomplete"})
    assert response.status_code == 400
