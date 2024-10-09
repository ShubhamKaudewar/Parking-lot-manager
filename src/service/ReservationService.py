from fastapi import FastAPI
from pydantic import BaseModel

from src.dao.vehicleDao import VehicleDao


# Define ParkingSpot model
class Reservation(BaseModel):
    parkingId: int
    vehicleId: int

class ReservationUpdate(BaseModel):
    startTime: int | None = None
    endTime: int | None = None
    parkingId: str | None = None
    vehicleId: str | None = None

app = FastAPI()
from src.dao.reservationDao import ReservationDao


@app.get("/reservation/")
async def get_all_vehicles_details():
    response = VehicleDao().get_all_vehicle_details()
    return {"status": "success", "data": response}

@app.get("/reservation/{id}")
def get_all_vehicles_details_by_id(id: int):
    response = VehicleDao().get_all_vehicles_details_by_id(id)
    return response

@app.post("/reservation/")
async def create_reservation_details(data: Reservation):
    from src.util.date_util import current_time_in_millis
    start_time = current_time_in_millis()
    end_time = start_time + 2*3600000
    request = {
        "parkingId": data.parkingId,
        "vehicleId": data.vehicleId,
        "startTime": start_time,
        "endTime": end_time,
    }
    print("request", request)
    response = ReservationDao().create_reservation_details(request)
    return response

@app.put("/reservation/{id}")
async def update_parking_spot_details_by_id(id: int, data: ReservationUpdate):
    request = {
        "licensePlate": data.licensePlate,
        "ownerName": data.ownerName,
        "vehicleType": data.vehicleType,
    }
    print("parking spot details update for ID:", id, "data:", request)
    response = VehicleDao().update_vehicle_details_by_id(id, request)
    print("response", response)
    return response

@app.delete("/reservation/{id}")
async def delete_reservation_details(id: int):
    response = ReservationDao().delete_reservation_details_by_id(id)
    return response