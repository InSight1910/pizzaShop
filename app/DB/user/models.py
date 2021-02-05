from .. import db

collection = db["user"]


def get_user(username):
    result = collection.find({"username": username})[0]
    result["_id"] = str(result["_id"])
    return result