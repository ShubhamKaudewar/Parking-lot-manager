from fastapi import FastAPI, APIRouter, Request
from pydantic import BaseModel
from .limiterService import limiter

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

router = APIRouter(prefix="/parking-spot")

@router.get("")
@limiter.limit("1/second")
async def get_all_parking_spots(request: Request) -> dict:
    response = ParkingSpotDao().get_all_parking_spot_details()
    return {"status": "success", "data": response}

@router.get("/available")
@limiter.limit("1/second")
async def get_all_available_parking_spots(request: Request) -> dict:
    response = ParkingSpotDao().get_all_available_parking_spots()
    return response

@router.get("/{id}")
@limiter.limit("1/second")
def get_parking_spot_by_id(request: Request, id: int) -> dict:
    response = ParkingSpotDao().get_parking_spot_details_by_id(id)
    return response

@router.get("/{id}/status")
@limiter.limit("10/second")
def get_parking_spot_by_id(request: Request, id: int) -> dict:
    response = ParkingSpotDao().get_parking_spot_status_by_id(id)
    return response


@router.post("/")
@limiter.limit("1/second")
async def create_parking_spot(request: Request, data: ParkingSpot) -> dict:
    request = {
        "spotNumber": data.spotNumber,
        "status": data.status,
        "vehicleType": data.vehicleType,
    }
    print("request", request)
    ParkingSpotDao().create_parking_spot(request)
    return {"status": "success", "data": request}


@router.put("/{id}")
@limiter.limit("1/second")
async def update_parking_spot_details_by_id(request: Request, id: int, data: ParkingSpotUpdate) -> dict:
    request = {
        "spotNumber": data.spotNumber,
        "status": data.status,
        "vehicleType": data.vehicleType,
    }
    print("parking spot details update for ID:", id, "data:", request)
    response = ParkingSpotDao().update_parking_spot_details_by_id(id, request)
    print("response", response)
    return response

@router.delete("/{id}")
@limiter.limit("1/second")
async def delete_parking_spot(request: Request, id: int) -> dict:
    response = ParkingSpotDao().delete_parking_spot_details_by_id(id)
    return response
