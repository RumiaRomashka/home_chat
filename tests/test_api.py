from fastapi.testclient import TestClient

#from src.main import app
#from src.db import get_session

from src.main import app
from src.db import get_session


def test_test_db(mock_session):
    def get_session_override():
        return mock_session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)

    response = client.get("/test")

    app.dependency_overrides.clear()

    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["db_response"] == 1