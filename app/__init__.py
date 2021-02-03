from flask import Flask
from app.config import Config

from .products import products


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(products)
    return app