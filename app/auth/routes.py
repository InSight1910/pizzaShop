from . import auth
from app.DB.auth.models import sign_up

from flask import request


@auth.route("signup", methods=["POST"])
def signUp():
    result = sign_up(request.json)
    return result