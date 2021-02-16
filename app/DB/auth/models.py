from .. import db

from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import secrets, jwt
from ...config import Config
from flask import request
from email_validator import EmailNotValidError, validate_email
from datetime import datetime, timedelta

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
        valid_email = validate_email(body["email"])
        inserted_user = {
            "_id": ObjectId(id),
            "name": body["name"],
            "username": body["username"],
            "email": valid_email.email,
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

        result = collection_user.find_one({"_id": inserted_auth["_id"]})
        result["_id"] = str(result["_id"])
        return result
    except DuplicateKeyError as e:
        return {
            "error": True,
            "message": str(e),
        }
    except EmailNotValidError as e:
        return {
            "error": True,
            "message": str(e),
        }


def sign_in():
    auth = request.authorization
    username, password = auth["username"], auth["password"]
    auth = collection_auth.find_one({"username": username})
    if check_password_hash(pwhash=auth["password"], password=password):
        timeLimit = datetime.utcnow() + timedelta(minutes=30)
        user = collection_user.find_one({"username": username})
        payload = {
            "_id": str(user["_id"]),
            "exp": timeLimit,
        }

        token = jwt.encode(payload, Config.SECRET_KEY)
        return_data = {
            "error": "0",
            "message": "Successful",
            "token": token,
            "Elapse_time": f"{timeLimit}",
        }
        return return_data


def get_user_auth(id):
    result = collection_auth.find_one({"_id": ObjectId(id)})
    result["_id"] = str(result["_id"])
    return result