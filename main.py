from app.DB.product.models import *
from app.DB.user.models import *
from app.DB.auth.models import *
from flask import redirect, request
import time

from app import create_app
from app.utils.securityJWT import token_required

app = create_app()


@app.route("/", methods=["POST", "GET"])
def index():
    return {}


@app.route("/lll", methods=["GET"])
@token_required
def index1(f):
    return get_products()


@app.route("/changePassword")
def password():
    user_id = request.args.get("user_id")
    token = request.args.get("token")

    return changing_password(token, user_id, request.data.decode())


@app.errorhandler(404)
def notFound(error):
    redirect("")
