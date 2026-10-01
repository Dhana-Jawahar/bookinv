from fastapi.testclient import TestClient
from bookInvapi.main import app
from bookInvapi.routers.bookcrud import router
client=TestClient(app)
import pytest

def test_get_books():
    app.include_router(router)
   
    client = TestClient(app)
    response = client.get("/Book/")

# A mock dependency to replace your real database session
def override_get_db():
    try:
        db = MockDatabaseSession()
        yield db
    finally:
        db.close()

    assert response.status_code == 200
    assert response.json() == [{
        "title": "Rooftoppers",
        "bookid": 1,
        "isbn": "9781526624802",
        "author": "Katherine Rundell",
        "price": 35,
        "quantity": 10,
    }]


