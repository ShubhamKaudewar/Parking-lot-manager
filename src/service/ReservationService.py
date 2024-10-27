from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

from src.dao.vehicleDao import VehicleDao


# Define ParkingSpot model
class Reservation(BaseModel):
    parkingId: int
    vehicleId: int

class ReservationUpdate(BaseModel):
    vehicleId: int | None = None
    parkingId: int | None = None
    startTime: int | None = None
    endTime: int | None = None

app = FastAPI()

router = APIRouter(prefix="/reservation")
from src.dao.reservationDao import ReservationDao


@router.get("")
async def get_all_reservation_details():
    response = ReservationDao().get_all_reservation_details()
    return response

@router.get("/{id}")
def get_reservation_details_by_id(id: int):
    response = ReservationDao().get_reservation_details_by_id(id)
    return response

@router.post("/")
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

@router.put("/{id}")
async def update_reservation_details_by_id(id: int, data: ReservationUpdate):
    request = {
        "parkingId": data.parkingId,
        "vehicleId": data.vehicleId
    }
    from src.util.date_util import get_millis_from_date_string
    if data.startTime:
        start_time = get_millis_from_date_string(data.startTime)
        request["startTime"] = start_time
    if data.endTime:
        end_time = get_millis_from_date_string(data.endTime)
        request["endTime"] = end_time
    print("Reservation details update for ID:", id, "data:", request)
    response = ReservationDao().update_registration_details_by_id(id, request)
    print("response", response)
    return response

@router.delete("/{id}")
async def delete_reservation_details(id: int):
    response = ReservationDao().delete_reservation_details_by_id(id)
    return response