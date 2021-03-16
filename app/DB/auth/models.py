from app.utils.utils import create_product_object, create_user_object
from .. import db

from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from ...config import Config
from flask import request
from email_validator import EmailNotValidError, validate_email
from datetime import datetime, timedelta

collection_auth = db["authentication"]
collection_user = db["user"]


def sign_up(body):
    if "name" not in body:
        return {"error": True, "body": "You must provide a name"}, 405
    if "username" not in body:
        return {"error": True, "body": "You must provide a username"}, 405
    if "email" not in body:
        return {"error": True, "body": "You must provide a email"}, 405
    if "address" not in body:
        return {"error": True, "body": "You must provide a address"}, 405
    try:

        valid_email = validate_email(body["email"])
        inserted_user = {
            "name": body["name"],
            "username": body["username"],
            "email": valid_email.email,
            "address": body["address"],
            "orders": [],
        }
        document_user = collection_user.insert_one(inserted_user)

        inserted_auth = {
            "_id": ObjectId(document_user.inserted_id),
            "username": body["username"],
            "password": generate_password_hash(password=body["password"]),
        }
        document_auth = collection_auth.insert_one(inserted_auth)

        result = collection_user.find_one({"_id": document_user.inserted_id})
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
        }, 405


def sign_in():
    auth = request.authorization
    username, password = auth["username"], auth["password"]
    auth = collection_auth.find_one({"username": username})
    if check_password_hash(pwhash=auth["password"], password=password):
        timeLimit = datetime.utcnow() + timedelta(minutes=30)
        user = collection_user.find_one({"username": username})
        payload = {
            "user": create_user_object(user),
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