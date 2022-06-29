from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_all_todos():
    response = client.get("/todo")
    assert response.status_code == 200


def test_get_todo():
    response = client.get("/todo/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 1
    assert type(json_data["task"]) == str


def test_post_todo():
    response = client.post("/todo", json={"task": "POST test new task"})
    assert response.status_code == 201
    json_data = response.json()
    assert type(json_data["id"]) == int
    assert json_data["task"] == "POST test new task"


def test_put_todo():
    response = client.put("/todo/2?task=PUT test edit task")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 2
    assert json_data["task"] == "PUT test edit task"


def test_delete_todo():
    response = client.delete("/todo/10")
    assert response.status_code == 204
