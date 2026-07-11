from flask import Flask
from src.main.routes.users_route import user_routes

app = Flask(__name__)

app.register_blueprint(user_routes)