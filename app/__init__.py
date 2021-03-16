from flask import Flask, request

from flask_mail import Mail
from app.config import Config

from .products import products
from .auth import auth

from flask_swagger_ui import get_swaggerui_blueprint

mail = Mail()

SWAGGER_URL = ""
API_URL = "/static/swagger.json"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Pizza Shop"}
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(products)
    app.register_blueprint(auth)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    mail.init_app(app)
    return app
