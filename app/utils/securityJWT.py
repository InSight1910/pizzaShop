from bson.objectid import ObjectId
from werkzeug.security import safe_str_cmp
from app.models import AuthData
from werkzeug.security import check_password_hash
from app.DB import db
from .utils import create_auth_object, create_product_object, create_user_object


collection_auth = db["authentication"]
collection_user = db["user"]


def authentication(username, password):
    try:
        result = collection_auth.find({"username": username}).next()
        user = create_auth_object(result)
        if user and check_password_hash(user.password, password):
            return user
    except StopIteration:
        return {"error": True, "message": "Username not found"}


def identity(payload):
    user_id = payload["identity"]
    result_auth = collection_auth.find({"_id": ObjectId(user_id)})[0]["user_id"]
    result_user = collection_user.find({"id": result_auth})[0]
    user = create_user_object(result_user)
    return user