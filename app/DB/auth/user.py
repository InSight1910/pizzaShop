from flask_login import UserMixin
from .. import db


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        self.username = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(username):
        user = db["authentication"].find({"username": username})[0]
        user_data = UserData(user["username"], user["password"])
        return UserModel(user_data)

    def get_id(self):
        return self.username