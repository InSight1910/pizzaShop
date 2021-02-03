from app import create_app
from app.DB.product.models import get_products
from flask import redirect
app = create_app()
@app.route('/')
def index():
    return get_products()

@app.errorhandler(404)
def notFound(error):
    redirect('')