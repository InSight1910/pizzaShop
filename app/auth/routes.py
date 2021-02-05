from flask_login.utils import logout_user
from . import auth
from app.DB.auth.models import login, sign_up
from flask import request


@auth.route("login", methods=["POST"])
def log():
    result = login(request.json)
    return result


@auth.route("signup", methods=["POST"])
def signup():
    result = sign_up(request.json)
    return result


@auth.route("logout")
def log_out():
    logout_user()
    return {}