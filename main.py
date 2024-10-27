from fastapi import FastAPI, APIRouter
from src.service.VehicleService import router as vehicle_router
from src.service.ReservationService import router as reservation_router
from src.service.ParkingSpotService import router as parking_router
from src.service.limiterService import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

main_router = APIRouter()
app = FastAPI()

app.include_router(vehicle_router)
app.include_router(reservation_router)
app.include_router(parking_router)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
def read_root():
    return "Server is running."

