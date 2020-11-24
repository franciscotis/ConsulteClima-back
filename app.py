from flask import Flask
from src.routes.routes import define_routes
app = Flask(__name__)

define_routes(app)