from bson import ObjectId
from flask import jsonify


class AuthData:
    def __init__(self, id, username, password):
        self.id = str(id)
        self.username = username
        self.password = password

    def auth(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }


class UserData:
    def __init__(self, _id, username, name, email, address, orders):
        self._id = str(_id)
        self.username = username
        self.name = name
        self.email = email
        self.address = address
        self.orders = orders

    def user(self):
        return {
            "id": self._id,
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "orders": self.orders,
        }


class ProductData:
    def __init__(self, id, name, extra_ingredients):
        self._id = str(id)
        self.name = name

        self.extra_ingredients = extra_ingredients

    def product(self):
        return {
            "_id": self._id,
            "name": self.name,
            "extra_ingredients": self.extra_ingredients,
        }


class Token:
    def __init__(self, id, token, createdAt):
        self._id = ObjectId(id)
        self.token = token
        self.createdAt = createdAt

    def tokens(self):
        return {
            "_id": self._id,
            "token": self.token,
            "created_at": self.createdAt,
        }
