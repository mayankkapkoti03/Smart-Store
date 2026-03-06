from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "email": "test6user@example.com",
            "password": "testpassword"
        }
    )
    print(response.json())
    assert response.status_code == 200


#Login test for valid credentials
def test_login_user():
    response = client.post(
        "/auth/login",
        data={
            "username": "test3user@example.com",
            "password": "testpassword"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()