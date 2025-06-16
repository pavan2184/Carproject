from fastapi import FastAPI
from structure import Car
from database import dataset, convert
from bson import ObjectId

app = FastAPI()

@app.post("/cars")
def add(car:Car):
    result = dataset.insert_one(car)  # Convert Car to dict and insert
    return "Car has been added with ID" + str(result.inserted_id)      # Return the inserted ID

@app.get("/cars")
def get_all_cars():
    all = [convert(car) for car in dataset.find()]
    return all

@app.get("/cars/specific")
def get_car(id):
    car = dataset.find_one({"_id": ObjectId(id)})
    if car:
        return convert(car)
    return "Car not found"

@app.delete("/cars/delete")
def delete_car(id):
    result = dataset.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return "Car deleted"
    return "Car not found"
