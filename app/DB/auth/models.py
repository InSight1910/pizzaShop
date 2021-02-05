from .. import db
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

from .user import UserData, UserModel

collection_auth = db["authentication"]
collection_user = db["user"]


def login(body):
    if "username" in body:
        if "password" in body:
            querry_auth = {
                "username": body["username"],
            }
            result_auth = collection_auth.find(querry_auth)[0]
            if check_password_hash(result_auth["password"], body["password"]):
                querry_user = {
                    "id": result_auth["user_id"],
                }
                result = collection_user.find(querry_user)[0]
                result["_id"] = str(result["_id"])
                user_data = UserData(result_auth["username"], result_auth["password"])
                user = UserModel(user_data)
                login_user(user)
                return result
            return {"error": True, "body": "Invalid password provided"}
        return {"error": True, "body": "You have to provide a password"}
    return {"error": True, "body": "You have to provide a valid username"}


def sign_up(body):
    user_id = secrets.token_hex(32)
    inserted_user = {
        "id": user_id,
        "name": body["name"],
        "username": body["username"],
        "email": body["email"],
        "address": body["address"],
        "orders": [],
    }
    inserted_auth = {
        "user_id": user_id,
        "username": body["username"],
        "password": generate_password_hash(password=body["password"]),
    }
    if (
        collection_auth.find({"username": body["username"]}).count() == 0
        or collection_user.find({"username": body["username"]}).count() == 0
    ):
        collection_auth.insert_one(inserted_auth)
        collection_user.insert_one(inserted_user)
        result = collection_user.find({"id": inserted_auth["user_id"]})[0]
        result["_id"] = str(result["_id"])
        return result
    return {"error": True, "body": "The username is already registered"}


def get_user_auth(username):
    result = collection_auth.find({"username": username})[0]
    result["_id"] = str(result["_id"])
    return result