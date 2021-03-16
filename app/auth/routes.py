from app.DB.user.models import change_password, changing_password
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


@auth.route("change_password", methods=["POST"])
def change_passwords():
    if request.args.get("user_id") or request.args.get("token"):
        user_id = request.args.get("user_id")
        token = request.args.get("token")

        return changing_password(token, user_id, request.json["password"])
    return change_password()


@auth.errorhandler(404)
def not_found(error):
    return {
        "error": True,
        "body": "Sorry the page you are trying to access was not found",
        "message": str(error),
    }
