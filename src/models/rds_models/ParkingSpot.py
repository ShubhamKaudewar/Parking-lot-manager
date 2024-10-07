"""
Class for Parking Spot
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()
Base = mapper_registry.generate_base()


class ParkingSpot(Base):
    __tablename__ = "parkingSpot"

    parkingId = Column(Integer, primary_key=True)
    spotNumber = Column(Integer)
    status = Column(String(255))
    vehicleType = Column(String(255))

    # relationship
    reservation = relationship("Reservation", backref="parkingSpot")
