import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/car_database")

client = MongoClient(MONGO_URL)
dataset = client.get_database().get_collection("cars")



def convert(car) :
    return {
        "id": str(car["_id"]),
        "brand": car["brand"],
        "model": car["model"],
        "colour" : car["colour"],
        "year": car["year"]
    }

