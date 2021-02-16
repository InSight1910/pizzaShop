from flask import request, jsonify
from ..config import Config
from app.DB.auth.models import get_user_auth
from functools import wraps
import jwt


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if "token" in request.headers:
            token = request.headers["token"]

        if not token:
            return jsonify({"message": "a valid token is missing"})

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_user = get_user_auth(data["_id"])
        except:
            return jsonify({"message": "token is invalid"})

        return f(current_user, *args, **kwargs)

    return decorator
