from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

from src.dao.vehicleDao import VehicleDao


# Define ParkingSpot model
class Vehicle(BaseModel):
    licensePlate: str
    vehicleType: str
    ownerName: str

class VehicleUpdate(BaseModel):
    licensePlate: str | None = None
    vehicleType: str | None = None
    ownerName: str | None = None

app = FastAPI()
from src.dao.parkingSpotDao import ParkingSpotDao


@app.get("/vehicle/")
async def get_all_vehicles_details():
    response = VehicleDao().get_all_vehicle_details()
    return {"status": "success", "data": response}

@app.get("/vehicle/{id}")
def get_all_vehicles_details_by_id(id: int):
    response = VehicleDao().get_all_vehicles_details_by_id(id)
    return response

@app.post("/vehicle/")
async def create_vehicle_details(data: Vehicle):
    request = {
        "licensePlate": data.licensePlate,
        "ownerName": data.ownerName,
        "vehicleType": data.vehicleType,
    }
    print("request", request)
    response = VehicleDao().create_vehicle_details(request)
    return response

@app.put("/vehicle/{id}")
async def update_parking_spot_details_by_id(id: int, data: VehicleUpdate):
    request = {
        "licensePlate": data.licensePlate,
        "ownerName": data.ownerName,
        "vehicleType": data.vehicleType,
    }
    print("parking spot details update for ID:", id, "data:", request)
    response = VehicleDao().update_vehicle_details_by_id(id, request)
    print("response", response)
    return response

@app.delete("/vehicle/{id}")
async def delete_vehicle_details(id: int):
    response = VehicleDao().delete_vehicle_details_by_id(id)
    return response