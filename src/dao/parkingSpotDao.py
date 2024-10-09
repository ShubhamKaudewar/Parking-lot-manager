from src.models.rds_models import Session, Vehicle, ParkingSpot
import logging
logger = logging.getLogger(__name__)


class ParkingSpotDao:
    """
    Class to handle data queries for API in context.
    """
    def __init__(self):
        super().__init__()
        self.session = Session()

    def get_all_parking_spot_details(self):
        qry_object = self.session.query(ParkingSpot).all()
        results = []
        for obj in qry_object:
            results.append({
                "parkingId": obj.parkingId,
                "spotNumber": obj.spotNumber,
                "status": obj.status,
                "vehicleType": obj.vehicleType
            })
        return results

    def get_all_available_parking_spots(self):
        qry_object = self.session.query(ParkingSpot).all()
        spots_available = [i for i in range(1, 20)]
        for obj in qry_object:
            spots_available.remove(obj.spotNumber)
        response = {"status": "success", "data": spots_available}
        return response

    def get_parking_spot_details_by_id(self, parking_id):
        qry_object = self.session.query(ParkingSpot).filter(ParkingSpot.parkingId == parking_id)
        if qry_object.first():
            obj = qry_object.first()
            response = {
                "status": "success",
                "data": {
                    "parkingId": obj.parkingId,
                    "spotNumber": obj.spotNumber,
                    "status": obj.status,
                    "vehicleType": obj.vehicleType
                }
            }
        else:
            response = {
                "status": "failure",
                "message": f"No details found for id:{parking_id}"
            }
        return response

    def get_parking_spot_status_by_id(self, parking_id):
        qry_object = self.session.query(ParkingSpot).filter(ParkingSpot.parkingId == parking_id)
        if qry_object.first():
            obj = qry_object.first()
            response = {
                "status": "success",
                "parkingSpotStatus": obj.status
            }
        else:
            response = {
                "status": "failure",
                "message": f"No details found for id:{parking_id}"
            }
        return response

    def get_vehicle_details_from_number_plate(self, number_plate):
        details = self.session.query(Vehicle).filter(Vehicle.licensePlate == number_plate).all()
        return details

    def create_parking_spot(self, data):
        new_parking_spot = ParkingSpot(
            spotNumber=data.get("spotNumber"),
            status=data.get("status"),
            vehicleType=data.get("vehicleType")
        )
        qry_object = self.session.query(ParkingSpot)\
            .filter(ParkingSpot.spotNumber == new_parking_spot.spotNumber)

        if qry_object.first() is None:
            self.session.add(new_parking_spot)
        else:
            qry_object.update(new_parking_spot)

        import sqlalchemy as sa
        try:
            self.session.commit()
        except sa as e:
            logger.error(e.args)
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def update_parking_spot_details_by_id(self, parking_id, data):
        qry_object = self.session.query(ParkingSpot)\
            .filter(ParkingSpot.parkingId == parking_id)

        if qry_object.first():
            obj = qry_object.first()
            if data.get("spotNumber"):
                obj.spotNumber = data.get("spotNumber")
            if data.get("status"):
                obj.status = data.get("status")
            if data.get("vehicleType"):
                obj.vehicleType = data.get("vehicleType")
            response = {
                "status": "success",
                "message": f"Parking spot details of id:{parking_id} updated successfully!"
            }

            import sqlalchemy as sa
            try:
                self.session.commit()
            except sa as e:
                logger.error(e.args)
                self.session.rollback()
                return False
            finally:
                self.session.close()
        else:
            response = {
                "status": "failure",
                "message": f"No details found for id:{parking_id}"
            }
        return response

    def delete_parking_spot_details_by_id(self, parking_id):
        qry_object = self.session.query(ParkingSpot)\
            .filter(ParkingSpot.parkingId == parking_id)

        if qry_object.first():
            qry_object.delete(synchronize_session=False)

            import sqlalchemy as sa
            try:
                self.session.commit()
            except sa as e:
                logger.error(e.args)
                self.session.rollback()
                return False
            finally:
                self.session.close()
            response = {
                "status": "success",
                "message": f"Parking spot details of id:{parking_id} deleted successfully!"
            }
        else:
            response = {
                "status": "failure",
                "message": f"No details found for id:{parking_id}"
            }
        return response