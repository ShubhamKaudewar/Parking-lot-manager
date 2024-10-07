from src.dao.parking_lot_dao import ParkingLotDao


class ParkingLotService:
    def __init__(self):
        super().__init__()

    def get_owner_name(self, number_plate):
        details = ParkingLotDao().get_vehicle_details_from_number_plate(number_plate)
        name = details[0].ownerName
        print("Owner is:", name)
        return {"ownerName": name}
