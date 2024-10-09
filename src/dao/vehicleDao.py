from src.models.rds_models import Session, Vehicle, ParkingSpot
import logging
logger = logging.getLogger(__name__)


class VehicleDao:
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

    def get_vehicle_details_from_vehicle_id(self, vehicle_id):
        details = self.session.query(Vehicle).filter(Vehicle.vehicleId == vehicle_id).first()
        response = {
            "vehicleId": details.vehicleId,
            "licensePlate": details.licensePlate,
            "vehicleType": details.vehicleType,
            "ownerName": details.ownerName,
        }
        return response

    def create_vehicle_details(self, data):
        license_plate = data.get("licensePlate")
        new_vehicle_details = Vehicle(
            licensePlate=data.get("licensePlate"),
            vehicleType=data.get("vehicleType"),
            ownerName=data.get("ownerName")
        )
        qry_object = self.session.query(Vehicle)\
            .filter(Vehicle.licensePlate == license_plate)

        response = []
        if qry_object.first() is None:
            self.session.add(new_vehicle_details)

            import sqlalchemy as sa
            try:
                self.session.commit()
            except sa as e:
                logger.error(e.args)
                self.session.rollback()
                return False
            finally:
                self.session.close()
            vehicle_data = self.get_vehicle_details_from_number_plate(license_plate)
            response.append({
                "status": "success",
                "message": "Successfully created vehicle details!",
                "data": vehicle_data
            })
        else:
            response.append({
                "status": "failure",
                "message": "Data already exist!",
            })
        return response[0]

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

    def delete_vehicle_details_by_id(self, vehicle_id):
        qry_object = self.session.query(Vehicle)\
            .filter(Vehicle.vehicleId == vehicle_id)

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
                "message": f"Vehicle details of id:{vehicle_id} deleted successfully!"
            }
        else:
            response = {
                "status": "failure",
                "message": f"No details found for id:{vehicle_id}"
            }
        return response
