from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.DB_URI)

db = client['pizzaShop']

from .product import models