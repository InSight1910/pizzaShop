from .. import db

from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import secrets


collection_auth = db["authentication"]
collection_user = db["user"]


def sign_up(body):
    if "name" not in body:
        return {"error": True, "body": "You must provide a name"}
    if "username" not in body:
        return {"error": True, "body": "You must provide a username"}
    if "email" not in body:
        return {"error": True, "body": "You must provide a email"}
    if "address" not in body:
        return {"error": True, "body": "You must provide a address"}
    """ if not (
        collection_auth.find({"username": body["username"]}).count() == 0
        and collection_user.find({"username": body["username"]}).count() == 0
    ):
        return {"error": True, "body": "The username is already registered"} """
    """ if not collection_user.find({"email": body["email"]}).count() == 0:
        return {"error": True, "body": "The email is already registered"} """
    try:
        id = secrets.token_hex(12)

        inserted_user = {
            "_id": ObjectId(id),
            "name": body["name"],
            "username": body["username"],
            "email": body["email"],
            "address": body["address"],
            "orders": [],
        }
        inserted_auth = {
            "_id": ObjectId(id),
            "username": body["username"],
            "password": generate_password_hash(password=body["password"]),
        }
        collection_auth.insert_one(inserted_auth)
        collection_user.insert_one(inserted_user)

        result = collection_user.find({"id": inserted_auth["_id"]})[0]
        result["_id"] = str(result["_id"])
        return result
    except DuplicateKeyError:
        return {}