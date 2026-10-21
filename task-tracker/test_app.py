from app import app


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Task Tracker" in response.data


def test_task_input_exists():
    client = app.test_client()
    response = client.get("/")

    assert b'id="taskInput"' in response.data
    assert b"Add Task" in response.data


def test_task_list_exists():
    client = app.test_client()
    response = client.get("/")

    assert b'id="taskList"' in response.data
    assert b"No tasks added yet." in response.data


def test_task_functions_exist():
    client = app.test_client()
    response = client.get("/")

    assert b"function addTask()" in response.data
    assert b"function updateEmptyMessage()" in response.data
