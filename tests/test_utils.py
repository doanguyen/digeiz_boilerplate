from flask import Flask, jsonify
from flask.views import MethodView

from digeiz_api.utils import register_api


class TestMethodView(MethodView):
    def get(self):
        return jsonify({})

    post = put = patch = delete = get


def test_register_api():
    app = Flask(__name__)
    register_api(app, TestMethodView, "test_endpoint", "/api/test")
    client = app.test_client()
    get_response = client.get("/api/test")
    assert get_response.status_code == 200
    assert client.post("/api/test", json={}).status_code == 200
    assert client.put("/api/test", json={}).status_code == 200
    assert client.patch("/api/test", json={}).status_code == 200
    assert client.delete("/api/test", json={}).status_code == 200
