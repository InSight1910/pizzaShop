from . import auth
from app.DB.auth.models import sign_up, sign_in

from flask import request


@auth.route("signup", methods=["POST"])
def signUp():
    result = sign_up(request.json)
    return result


@auth.route("signin", methods=["POST"])
def signIn():
    result = sign_in()
    return result