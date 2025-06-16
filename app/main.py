from fastapi import FastAPI
from app.structure import Car
from app.database import dataset, convert
from bson import ObjectId

app = FastAPI()

@app.post("/cars")
def add(car:Car):
    result = dataset.insert_one(car.model_dump())  
    return "Car has been added with ID" + str(result.inserted_id)  

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
