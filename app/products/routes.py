from . import products
from app.DB.product.models import (
    get_products,
    get_products_by_id,
    get_products_for_name,
    create_product,
    remove_product_by_id,
    remove_product_by_name,
    update_product_by_name,
    update_product_by_id,
)

from flask_jwt import jwt_required
from flask import request


@products.route("")
def all():
    result = get_products()
    return result


@products.route("", methods=["POST"])
@jwt_required()
def create_products():
    result = create_product(request.json)
    return result


@products.route("name/<name>", methods=["GET", "DELETE", "PUT"])
def name(name):
    if request.method == "GET":
        return get_products_for_name(name)
    if request.method == "DELETE":
        return remove_product_by_name(name)
    if request.method == "PUT":
        return update_product_by_name(name, request.json)


@products.route("id/<id>", methods=["GET", "DELETE", "PUT"])
def id(id):
    if request.method == "GET":
        return get_products_by_id(id)
    if request.method == "DELETE":
        return remove_product_by_id(id)
    if request.method == "PUT":
        return update_product_by_id(id, request.json)
