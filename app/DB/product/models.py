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


def update_product_by_name(name, new_body):
    old_product = collection.find({"name": name})
    if old_product.count() == 0:
        return {"error": True, "status": "Unsuccefully", "code": 404}
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
    print(collection.find({"name": updated_body["name"]}).count())
    if collection.find({"name": updated_body["name"]}).count() == 0:
        collection.update_one(
            {"name": name},
            {"$set": updated_body},
        )
        product = collection.find({"name": updated_body["name"]})[0]
        product["_id"] = str(product["_id"])
        return product
    return {}


def update_product_by_id(id, new_body):
    old_product = collection.find({"_id": ObjectId(id)})
    if old_product.count() == 0:
        return {"error": True, "status": "Unsuccefully", "code": 404}
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
        product = collection.find({"_id": ObjectId(id)})[0]
        product["_id"] = str(product["_id"])
        print(product)
        return product
    return {}