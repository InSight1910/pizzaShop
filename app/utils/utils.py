from ..models import AuthData, ProductData, UserData, Token


def create_product_object(result) -> dict:
    product = ProductData(
        result["_id"],
        result["name"],
        result["description"],
        result["extra_ingredients"],
    )
    return product.product()


def create_user_object(result) -> dict:
    user = UserData(
        result["_id"],
        result["username"],
        result["name"],
        result["email"],
        result["address"],
        result["orders"],
    )
    return user.user()


def create_auth_object(result) -> dict:
    auth = AuthData(result["_id"], result["username"], result["password"])
    return auth.auth()


def create_token_object(result) -> dict:
    token = Token(result["_id"], result["token"], result["created_at"])

    return token.tokens()