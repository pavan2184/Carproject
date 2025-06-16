from pymongo import MongoClient

# Create a client connection
client = MongoClient("mongodb://localhost:27017")
db = client["car_database"]
dataset = db["cars"]

# Serialize ObjectId and document into a dictionary

def convert(car) :
    return {
        "id": str(car["_id"]),
        "brand": car["brand"],
        "model": car["model"],
        "colour" : car["colour"],
        "year": car["year"]
    }

