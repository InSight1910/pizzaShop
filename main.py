from app import create_app
from app.DB.product.models import get_products
from app.DB.user.models import get_user, change_password, changing_password
from flask import redirect, request
import time

app = create_app()


@app.route("/")
def index():
    return change_password(request.data.decode())


@app.route("/changePassword")
def password():
    data = request.url.split("?")[1]
    token = data.split("token=")[1].split("&")[0]
    user_id = data.split("user_id=")[1]

    return changing_password(token, user_id, request.data.decode())


@app.errorhandler(404)
def notFound(error):
    redirect("")
