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


@app.get("/specific")
def get_one_car(id:str):
    car = dataset.find_one({"_id": ObjectId(id)})
    if car:
        return convert(car)