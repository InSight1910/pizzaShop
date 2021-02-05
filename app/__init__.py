from app import auth
from flask import Flask
from flask_login import LoginManager, login_manager
from app.config import Config

from .products import products
from .auth import auth
from app.DB.auth.user import UserModel

login = LoginManager()


@login.user_loader
def load_user(user):
    return UserModel.query(user)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(products)
    app.register_blueprint(auth)
    login.init_app(app)
    return app