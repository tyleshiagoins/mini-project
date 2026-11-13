import os
from hmac import compare_digest
from urllib.error import URLError
from urllib.request import urlopen

from flask import Flask, Response, request

app = Flask(__name__)
app.config["active_color"] = "blue"


@app.get("/")
@app.get("/static/deployment-version.txt")
def show_task_tracker():
    color = app.config["active_color"]
    service_url = os.environ[f"{color.upper()}_URL"].rstrip("/")
    page_url = service_url + request.path

    try:
        with urlopen(page_url, timeout=60) as page:
            response = Response(
                page.read(),
                content_type=page.headers.get("content-type"),
            )
    except (URLError, TimeoutError):
        return f"The {color} service is temporarily unavailable.", 502

    response.headers["x-deployment-color"] = color
    response.headers["cache-control"] = "no-store"
    return response


@app.post("/switch/<color>")
def switch_color(color):
    secret = os.environ.get("ROUTER_TOKEN", "")
    authorization = request.headers.get("authorization", "")
    expected_authorization = f"Bearer {secret}"

    if not secret or not compare_digest(
        authorization.encode(), expected_authorization.encode()
    ):
        return "Unauthorized.", 401

    if color not in ("blue", "green"):
        return "Choose blue or green.", 400

    app.config["active_color"] = color
    return {"active_color": color}
