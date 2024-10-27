from fastapi import FastAPI, APIRouter
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
router = APIRouter(prefix="/vehicle")
from src.dao.parkingSpotDao import ParkingSpotDao


@router.get("")
async def get_all_vehicles_details():
    response = VehicleDao().get_all_vehicle_details()
    return {"status": "success", "data": response}

@router.get("/{id}")
def get_vehicle_details_by_id(id: int):
    response = VehicleDao().get_vehicle_details_by_id(id)
    return response

@router.post("/")
async def create_vehicle_details(data: Vehicle):
    request = {
        "licensePlate": data.licensePlate,
        "ownerName": data.ownerName,
        "vehicleType": data.vehicleType,
    }
    print("request", request)
    response = VehicleDao().create_vehicle_details(request)
    return response

@router.put("/{id}")
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

@router.delete("/{id}")
async def delete_vehicle_details(id: int):
    response = VehicleDao().delete_vehicle_details_by_id(id)
    return response