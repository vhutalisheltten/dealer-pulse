from app import app


def test_product_details():
    client = app.test_client()
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json["name"] == "Roadster X"


def test_missing_product():
    client = app.test_client()
    assert client.get("/products/999").status_code == 404
