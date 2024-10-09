from rich.region import Region

from src.models.rds_models import Session, Vehicle, ParkingSpot, Reservation
import logging
logger = logging.getLogger(__name__)


class ReservationDao:
    """
    Class to handle data queries for API in context.
    """
    def __init__(self):
        super().__init__()
        self.session = Session()

    def get_all_vehicle_details(self):
        qry_object = self.session.query(Vehicle).all()
        results = []
        for obj in qry_object:
            results.append({
                "vehicleId": obj.vehicleId,
                "licensePlate": obj.licensePlate,
                "vehicleType": obj.vehicleType,
                "ownerName": obj.ownerName
            })
        return results

    def get_all_vehicles_details_by_id(self, vehicle_id):
        qry_object = self.session.query(Vehicle).filter(Vehicle.vehicleId == vehicle_id)
        if qry_object.first():
            obj = qry_object.first()
            response = {
                "status": "success",
                "data": {
                    "vehicleId": obj.vehicleId,
                    "licensePlate": obj.licensePlate,
                    "vehicleType": obj.vehicleType,
                    "ownerName": obj.ownerName
                }
            }
        else:
            response = {
                "status": "failure",
                "message": f"No details found for id:{vehicle_id}"
            }
        return response

    def get_vehicle_details_from_number_plate(self, number_plate):
        details = self.session.query(Vehicle).filter(Vehicle.licensePlate == number_plate).first()
        response = {
            "vehicleId": details.vehicleId,
            "licensePlate": details.licensePlate,
            "vehicleType": details.vehicleType,
            "ownerName": details.ownerName,
        }
        return response

    def get_reservation_details_from_ids(self, parking_id, vehicle_id):
        details = self.session.query(Reservation)\
            .filter(Reservation.parkingId == parking_id)\
            .filter(Reservation.vehicleId == vehicle_id)\
            .first()

        from src.util.date_util import get_date_in_string_from_millis
        start_time = get_date_in_string_from_millis(int(details.startTime))
        end_time = get_date_in_string_from_millis(int(details.endTime))
        response = {
            "reservationId": details.reservationId,
            "parkingId": details.parkingId,
            "vehicleId": details.vehicleId,
            "startTime": start_time,
            "endTime": end_time
        }
        return response


    def create_reservation_details(self, data):
        parking_id = data.get("parkingId")
        vehicle_id = data.get("vehicleId")

        from src.dao.parkingSpotDao import ParkingSpotDao
        parking_data = ParkingSpotDao().get_parking_spot_details_by_id(parking_id)
        if parking_data.get("status") == "failure":
            response = {
                "status": "failure",
                "message": f"No Parking spot data available of ID:{parking_id}"
            }
            return response

        from src.dao.vehicleDao import VehicleDao
        vehicle_data = VehicleDao().get_vehicle_details_by_id(vehicle_id)
        if vehicle_data.get("status") == "failure":
            response = {
                "status": "failure",
                "message": f"No Vehicle data available of ID:{vehicle_id}"
            }
            return response

        qry_object = self.session.query(Reservation)\
            .filter(Reservation.parkingId == parking_id)\
            .filter(Reservation.vehicleId == vehicle_id)

        if qry_object.first() is None:
            new_reservation_details = Reservation(
                parkingId=data.get("parkingId"),
                vehicleId=data.get("vehicleId"),
                startTime=data.get("startTime"),
                endTime=data.get("endTime")
            )
            self.session.add(new_reservation_details)

            import sqlalchemy as sa
            try:
                self.session.commit()
            except sa as e:
                logger.error(e.args)
                self.session.rollback()
                return False
            finally:
                self.session.close()
            reservation_data = self.get_reservation_details_from_ids(parking_id, vehicle_id)
            response = {
                "status": "success",
                "message": "Successfully created reservation details!",
                "data": reservation_data
            }
        else:
            response = {
                "status": "failure",
                "message": "Data already exist!",
            }
        return response

    def update_vehicle_details_by_id(self, vehicle_id, data):
        qry_object = self.session.query(Vehicle)\
            .filter(Vehicle.vehicleId == vehicle_id)

        if qry_object.first():
            obj = qry_object.first()
            if data.get("licensePlate"):
                obj.licensePlate = data.get("licensePlate")
            if data.get("ownerName"):
                obj.ownerName = data.get("ownerName")
            if data.get("vehicleType"):
                obj.vehicleType = data.get("vehicleType")
            response = {
                "status": "success",
                "message": f"Vehicle details of id:{vehicle_id} updated successfully!"
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
                "message": f"No details found for id:{vehicle_id}"
            }
        return response

    def delete_reservation_details_by_id(self, reservation_id):
        qry_object = self.session.query(Reservation)\
            .filter(Reservation.reservationId == reservation_id)

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
                "message": f"Reservation details of id:{reservation_id} deleted successfully!"
            }
        else:
            response = {
                "status": "failure",
                "message": f"No reservation details found for id:{reservation_id}"
            }
        return response
