import http
import os

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"

@app.route("/users")
def get_users_all():
    users = [
        {"id": 1, "name": "Juan Pérez", "telefono": "123-456-7890"},
        {"id": 2, "name": "María López", "telefono": "098-765-4321"},
        {"id": 3, "name": "Carlos García", "telefono": "555-123-4567"}
    ]

    user = {"id": 1, "name": "test", "telefono": "999-666-333"}
    print("traza 2")
    query = request.args.get('query')
    print("traza 3")
    if query:
        print("traza 4")
        user["query"] = query
    return jsonify(users), 200

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "999-666-333"}
    query = request.args.get('query')
    if query:
        print("traza 4")
        user["query"] = query
    return jsonify(user), 200


@app.route('/users/create', methods=['POST'])
def create_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), http.HTTPStatus.CREATED


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port, debug=False)
