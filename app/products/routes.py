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
from app.DB.user.models import (
    add_orders,
)


from flask import request
from ..utils.securityJWT import token_required


@products.route("")
def all():
    result = get_products()
    return result


@products.route("", methods=["POST"])
@token_required
def create_products(token):
    result = create_product(request.json)
    return result


@products.route("name/<name>", methods=["GET", "DELETE", "PUT"])
@token_required
def name(token, name):
    if request.method == "GET":
        return get_products_for_name(name)
    if request.method == "DELETE":
        return remove_product_by_name(name)
    if request.method == "PUT":
        return update_product_by_name(name, request.json)


@products.route("id/<id>", methods=["GET", "DELETE", "PUT"])
@token_required
def id(token, id):
    if request.method == "GET":
        return get_products_by_id(id)
    if request.method == "DELETE":
        return remove_product_by_id(id)
    if request.method == "PUT":
        return update_product_by_id(id, request.json)

    return {}


@products.route("addOrder", methods=["PUT"])
@token_required
def addOrder(token):
    return add_orders(
        request.json,
        token,
    )


@products.errorhandler(404)
def not_found(error):
    return {
        "error": True,
        "body": "Sorry the page you are trying to access was not found",
    }
