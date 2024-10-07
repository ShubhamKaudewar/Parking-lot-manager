
from src.service.parking_lot_service import ParkingLotService

if __name__ == "__main__":
    number_plate = "MH26CJ4474"
    data = ParkingLotService().get_owner_name(number_plate)
    print("name:", data.get("ownerName"))
