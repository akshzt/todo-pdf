import random
from main import app
from fastapi.testclient import TestClient



client = TestClient(app)

def test_todo_list():

    #get list
    get_list = client.get("/todo")
    assert get_list.status_code == 200

    #length of the list
    n = (len(get_list.json()))
    print(n)

    #all ids
    id_list = []
    for items in get_list.json():
        id_list.append(items["id"])

    #creating new item
    create_task_pl = "hmm new item here bro"
    create_new= client.post("/todo", json={"task":create_task_pl})
    assert create_new.status_code == 201
    after_create = client.get("/todo")
    create_len = len(after_create.json())
    assert create_len == n + 1

    #get item by ID
    payload_id = 1;
    response_get_by_id = {"id":1,"task":"this is my first task"}
    get_by_id = client.get(f"/todo/{payload_id}")
    assert get_by_id.status_code == 200
    assert get_by_id.json()["id"] == response_get_by_id["id"]
    assert get_by_id.json()["task"] == response_get_by_id["task"]

    #update by ID
    update_id_pl = random.choice(id_list)
    new_task_pl = "this is an updated task"
    update_by_id = client.put(f"/todo/{update_id_pl}?task={new_task_pl}")
    assert update_by_id.status_code == 202
    assert update_by_id.json()["task"] == new_task_pl
    print(f"Updated item with the id number {update_id_pl}")


    #delete by ID 
    delete_id_pl = random.choice(id_list)
    delete_by_id = client.delete(f"/todo/{delete_id_pl}")
    assert delete_by_id.status_code == 204
    after_delete = client.get("/todo")
    delete_len = len(after_delete.json())
    assert delete_len == n
    print(f"Deleted item with the id number {delete_id_pl}")



#negative testing
def test_negative():

    #get list fail
    get_list = client.get("/todo")
    id_list = []

    for items in get_list.json():
        id_list.append(items["id"])

    #non-existent id
    invalid_id = max(id_list) + 1


    #invalid get
    invalid_get = client.get(f"/todo/{invalid_id}")
    assert invalid_get.status_code == 404

    #invalid create
    invalid_create = client.post("/todo", json={"invalid_json":"that was not task"})
    assert invalid_create.status_code == 422

    #invalid update
    invalid_update = client.put(f"/todo/{invalid_id}?task=negative test task")
    assert invalid_update.status_code == 404
    invalid_update_json = client.put(f"/todo/{random.choice(id_list)}?invalid_property=this is not a task")
    assert invalid_update_json.status_code == 422

    #invalid delete
    invalid_delete = client.put(f"/todo/{invalid_id}")
    assert invalid_update.status_code == 404



















# def test_get_all_todos():
#     response = client.get("/todo")
#     assert response.status_code == 200


# def test_get_todo():
#     response = client.get("/todo/1")
#     assert response.status_code == 200
#     json_data = response.json()
#     assert json_data["id"] == 1
#     assert type(json_data["task"]) == str


# def test_post_todo():
#     response = client.post("/todo", json={"task": "POST test new task"})
#     assert response.status_code == 201
#     json_data = response.json()
#     assert type(json_data["id"]) == int
#     assert json_data["task"] == "POST test new task"


# def test_put_todo():
#     response = client.put("/todo/2?task=PUT test edit task")
#     assert response.status_code == 200
#     json_data = response.json()
#     assert json_data["id"] == 2
#     assert json_data["task"] == "PUT test edit task"


# def test_delete_todo():
#     response = client.delete("/todo/10")
#     assert response.status_code == 204
