from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

# Define ParkingSpot model
class ParkingSpot(BaseModel):
    spotNumber: int
    status: str
    vehicleType: str

class ParkingSpotUpdate(BaseModel):
    spotNumber: int | None = None
    status: str | None = None
    vehicleType: str | None = None

app = FastAPI()
from src.dao.parkingSpotDao import ParkingSpotDao


@app.get("/parking-spot/")
async def get_all_parking_spots():
    response = ParkingSpotDao().get_all_parking_spot_details()
    return {"status": "success", "data": response}

@app.get("/parking-spot/{id}")
def get_parking_spot_by_id(id: int):
    response = ParkingSpotDao().get_parking_spot_details_by_id(id)
    return response

@app.post("/parking-spot/")
async def create_parking_spot(data: ParkingSpot):
    request = {
        "spotNumber": data.spotNumber,
        "status": data.status,
        "vehicleType": data.vehicleType,
    }
    print("request", request)
    ParkingSpotDao().create_parking_spot(request)
    return {"status": "success", "data": request}


@app.put("/parking-spot/{id}")
async def update_parking_spot_details_by_id(id: int, data: ParkingSpotUpdate):
    request = {
        "spotNumber": data.spotNumber,
        "status": data.status,
        "vehicleType": data.vehicleType,
    }
    print("parking spot details update for ID:", id, "data:", request)
    response = ParkingSpotDao().update_parking_spot_details_by_id(id, request)
    print("response", response)
    return response

@app.delete("/parking-spot/{id}")
async def delete_parking_spot(id: int):
    response = ParkingSpotDao().delete_parking_spot_details_by_id(id)
    return response
