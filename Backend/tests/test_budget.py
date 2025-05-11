from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_budget():
    response = client.post("/budget/", json={"category": "Food", "limit": 500})
    assert response.status_code == 200
    assert response.json()["budget"]["category"] == "Food"