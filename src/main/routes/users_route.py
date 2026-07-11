from flask import Blueprint, jsonify

Blueprint("user_routes", __name__)

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["POST"])
def register_user():
    # Logic to register a new user
    return jsonify({"message": "User registered successfully"}), 200
