from flask import Flask, request

from flask_mail import Mail
from app.config import Config

from .products import products
from .auth import auth


mail = Mail()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(products)
    app.register_blueprint(auth)

    mail.init_app(app)
    return app
