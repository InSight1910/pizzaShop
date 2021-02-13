from .. import db
from bson import ObjectId
from app.utils.utils import create_product_object
from flask import jsonify

collection = db["products"]
extra_ingredients = [
    "Ham",
    "Pepperoni",
    "Chicken",
    "Pulled Pork",
    "Italian Sausage",
    "Beacon",
    "Black Olive",
    "Purple Onion",
    "Mushroom",
    "Corn",
    "Green Pepper",
    "Pineapple",
    "Tomato",
    "Tomato Cherry",
    "Extra Cheese",
    "BBQ Shot",
    "Shot of Pesto",
]


def get_products():
    results = collection.find({})
    products = []
    for re in results:
        product = create_product_object(re)
        products.append(product)
    return {"error": False, "body": products}


def get_products_for_name(name):
    if name == "":
        return {"error": True, "body": "You've to provide a product name"}
    try:
        results = collection.find({"name": name}).next()
        product = create_product_object(results)
        return {"error": False, "body": product.product()}
    except StopIteration:
        return {"error": True, "body": "We didn't find any product with that name"}


def get_products_by_id(id):
    if id != "":
        return {"error": True, "body": "You've to provide a product id "}
    try:
        results = collection.find({"_id": ObjectId(id)}).next()
        product = create_product_object(results)
        return {"error": False, "body": product}
    except StopIteration:
        return {"error": True, "body": "We did not find any product with that name"}


def create_product(body):
    if "name" not in body:
        return {"error": True, "body": "You have to provide a product name"}
    if "description" not in body:
        return {"error": True, "body": "You have to provide a product description"}
    if collection.find({"name": body["name"]}).count() == 0:
        return {"error": True, "body": "The product already exists"}

    product_inserted = {
        "name": body["name"],
        "description": body["description"],
    }
    product_inserted["extra_ingredients"] = extra_ingredients
    querry = collection.insert_one(product_inserted)
    result = get_products_by_id(querry.inserted_id)
    return {
        "error": False,
        "inserted_count_document": querry.acknowledged,
        "inserted_document": result,
    }


def remove_product_by_id(id):
    if id == "":
        return {"error": True, "body": "You have to provide a id of a product."}
    document = get_products_by_id(id)
    querry = collection.delete_one({"_id": ObjectId(id)})
    return {
        "error": False,
        "status": "Removed succesful",
        "documents_deleted": querry.deleted_count,
        "document_deleted": document,
    }


def remove_product_by_name(name):
    if name == "":
        return {"error": True, "body": "You have to provide a name of a product."}
    document = get_products_for_name(name)
    querry = collection.delete_one({"name": name})
    return {
        "error": False,
        "status": "Removed succesful",
        "documents_deleted": querry.deleted_count,
        "document_deleted": document,
    }


def update_product_by_name(name, new_body):
    old_product = collection.find({"name": name})
    if old_product.count() == 0:
        return {"error": True, "status": "Unsuccefully"}, 404
    old_product = old_product[0]
    updated_body = {"extra_ingredients": extra_ingredients}

    if "name" not in old_product:
        updated_body["name"] = old_product["name"]
    else:
        updated_body["name"] = new_body["name"]

    if "description" not in old_product:
        updated_body["description"] = old_product["description"]
    else:
        updated_body["description"] = new_body["description"]

    if collection.find({"name": updated_body["name"]}).count() == 0:
        collection.update_one(
            {"name": name},
            {"$set": updated_body},
        )
        result = collection.find({"name": updated_body["name"]})[0]
        product = create_product_object(result)
        return product
    return {"error": True, "message": "The name of the product already exists"}


def update_product_by_id(id, new_body):
    old_product = collection.find({"_id": ObjectId(id)})
    if old_product.count() == 0:
        return {"error": True, "status": "Unsuccefully", "code": 404}
    old_product = old_product[0]
    updated_body = {"extra_ingredients": extra_ingredients}
    for key in new_body.keys():
        if not key == "name":
            updated_body["name"] = old_product["name"]
        else:
            updated_body["name"] = new_body["name"]
        if not key == "description":
            updated_body["description"] = old_product["description"]
        else:
            updated_body["description"] = new_body["description"]

    if collection.find({"name": updated_body["name"]}).count() == 0:
        update = collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": updated_body},
        )
        result = collection.find({"_id": ObjectId(id)})[0]
        product = create_product_object(result)
        return product
    return {"error": True, "message": "The name of the product already exists"}
