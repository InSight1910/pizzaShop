from bson import ObjectId
from .. import db
from flask_mail import Message
from app.utils.utils import (
    create_user_object,
    create_token_object,
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from app.DB.product.models import (
    get_products_for_name,
)
import secrets, datetime

collection_user = db["user"]
collection_auth = db["authentication"]
collection_token = db["token"]
collection_products = db["products"]


def get_user(data):
    try:
        user = collection_user.find({"username": data}).next()
        user_object = create_user_object(user)
        return user_object
    except StopIteration:
        try:
            user = collection_user.find({"email": data}).next()
            user_object = create_user_object(user)
            return user_object
        except StopIteration:
            return {"error": True, "body": "User not found"}


def change_password(data):
    user = get_user(data)
    createdAt = datetime.datetime.now()
    token = secrets.token_hex(64)

    token_object = create_token_object(
        {
            "_id": user["_id"],
            "token": generate_password_hash(token),
            "created_at": createdAt,
        }
    )
    collection_token.insert_one(token_object)
    # Sending mail
    msg = Message(
        "Password request",
        sender="culadioe@gmail.com",
        recipients=["cvveglia@hotmail.com"],
    )
    msg.body = (
        f'http://localhost:5000/changePassword?token={token}&user_id={user["_id"]}'
    )
    from app import mail

    mail.send(msg)
    return msg.body


def changing_password(token, user_id, password):
    token_bd = collection_token.find({"_id": ObjectId(user_id)})[0]["token"]
    valid = check_password_hash(token_bd, token)
    if valid:
        hash_password = generate_password_hash(password)
        collection_auth.update_one(
            {"_id": ObjectId(user_id)}, {"$set": {"password": hash_password}}
        )
        return {}


def add_orders(data):
    try:
        user = get_user(data["user"])
        product = collection_products.find({"name": data["order"]["name"]}).next()
        order_object = {
            "name": product["name"],
            "price": 100,
            "amount": data["order"]["amount"],
            "status": "completed",
        }
        user["orders"].append(order_object)
        collection_user.update_one(
            {"_id": ObjectId(user["_id"])}, {"$set": {"orders": user["orders"]}}
        )
        return {}
    except StopIteration:
        return {"error": True}
