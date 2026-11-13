from unittest.mock import MagicMock

import router
from app import app


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Task Tracker" in response.data


def test_task_input_exists():
    client = app.test_client()
    response = client.get("/")

    assert b'<form id="task_form">' in response.data
    assert b'id="taskInput"' in response.data
    assert b'<button type="submit">Add task</button>' in response.data


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
    assert b"task_form.onsubmit" in response.data
    assert b'edit_button.textContent = "edit"' in response.data
    assert b'edit_button.textContent = "save"' in response.data
    assert b"edit_input.onkeydown" in response.data


def test_router_switches_to_green_and_back(monkeypatch):
    blue_url = "https://blue.example.com"
    green_url = "https://green.example.com"
    monkeypatch.setenv("BLUE_URL", blue_url)
    monkeypatch.setenv("GREEN_URL", green_url)
    monkeypatch.setenv("ROUTER_TOKEN", "test-token")
    monkeypatch.setitem(router.app.config, "active_color", "blue")

    # use a pretend page so the test can run without contacting Render
    open_page = MagicMock()
    page = open_page.return_value.__enter__.return_value
    page.headers = {"content-type": "text/html"}
    page.read.return_value = b"Task Tracker"
    monkeypatch.setattr(router, "urlopen", open_page)

    client = router.app.test_client()
    headers = {"authorization": "Bearer test-token"}

    assert client.get("/").headers["x-deployment-color"] == "blue"
    open_page.assert_called_with(f"{blue_url}/", timeout=60)

    assert client.post("/switch/green").status_code == 401
    assert client.get("/").headers["x-deployment-color"] == "blue"

    assert client.post("/switch/green", headers=headers).status_code == 200
    assert client.get("/").headers["x-deployment-color"] == "green"
    open_page.assert_called_with(f"{green_url}/", timeout=60)

    assert client.post("/switch/blue", headers=headers).status_code == 200
    assert client.get("/").headers["x-deployment-color"] == "blue"
    open_page.assert_called_with(f"{blue_url}/", timeout=60)
