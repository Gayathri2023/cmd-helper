import pytest
from fastapi.testclient import TestClient
from main import app   # your FastAPI file

client = TestClient(app)

def test_crud_user():

    # ---------------- CREATE ----------------
    create_response = client.post(
        "/users",
        json={"name": "Gayathri", "job": "QA"}
    )
    assert create_response.status_code == 201
    data = create_response.json()
    print("CREATE:", data)

    user_id = data["id"]

    # ---------------- READ ----------------
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    print("READ:", get_response.json())

    # ---------------- UPDATE ----------------
    update_response = client.put(
        f"/users/{user_id}",
        json={"name": "Gayathri", "job": "Senior QA"}
    )
    assert update_response.status_code == 200
    print("UPDATE:", update_response.json())

    # ---------------- DELETE ----------------
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 204
    print("DELETE SUCCESS")

    # ---------------- VERIFY DELETE ----------------
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404
