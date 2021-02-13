from flask import Flask
from flask_jwt import JWT
from flask_mail import Mail
from app.config import Config

from .products import products
from .auth import auth

from app.utils.securityJWT import authentication, identity

jwt = JWT(authentication_handler=authentication, identity_handler=identity)
mail = Mail()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(products)
    app.register_blueprint(auth)

    jwt.init_app(app)
    mail.init_app(app)

    return app