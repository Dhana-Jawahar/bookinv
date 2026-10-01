from fastapi.testclient import TestClient
from bookInvapi.main import app

client = TestClient(app)


def test_HealthCheck():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Book Inventory API is running..."}


