from src.models.rds_models import Session, Vehicle


class ParkingLotDao:
    """
    Class to handle data queries for API in context.
    """
    def __init__(self):
        super().__init__()
        self.session = Session()

    def get_vehicle_details_from_number_plate(self, number_plate):
        details = self.session.query(Vehicle).filter(Vehicle.licensePlate == number_plate).all()
        return details

