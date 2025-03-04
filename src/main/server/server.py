from flask import Flask
from src.main.server.routes.calculator import calc_route_bp

app = Flask(__name__)

app.register_blueprint(calc_route_bp)