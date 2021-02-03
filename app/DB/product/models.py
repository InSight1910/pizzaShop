from .. import db
from bson import ObjectId

collection = db["products"]


def get_products():
    results = collection.find()
    products = []
    for re in results:
        re["_id"] = str(re["_id"])
        products.append(re)
    return {"error": False, "body": products}


def get_products_for_name(name):
    results = collection.find({"name": name}).next()
    results["_id"] = str(results["_id"])
    return {"error": False, "body": results}


def get_products_by_id(id):
    results = collection.find({"_id": ObjectId(id)}).next()
    results["_id"] = str(results["_id"])
    return {"error": False, "body": results}


def create_product(body):
    product_inserted = {
        "name": body["name"],
        "description": body["description"],
    }
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
    product_inserted["extra_ingredients"] = extra_ingredients
    if collection.find({"name": body["name"]}).count() == 0:
        querry = collection.insert_one(product_inserted)
        result = get_products_by_id(querry.inserted_id)
        return {
            "error": False,
            "inserted_count_document": querry.acknowledged,
            "inserted_document": result,
        }
    return {"error": True, "body": "The product already exists"}


def remove_product_by_id(id):
    document = get_products_by_id(id)
    querry = collection.delete_one({"_id": ObjectId(id)})
    return {
        "error": False,
        "status": "Removed succesful",
        "documents_deleted": querry.deleted_count,
        "document_deleted": document,
    }


def remove_product_by_name(name):
    document = get_products_for_name(name)
    querry = collection.delete_one({"name": name})
    return {
        "error": False,
        "status": "Removed succesful",
        "documents_deleted": querry.deleted_count,
        "document_deleted": document,
    }
