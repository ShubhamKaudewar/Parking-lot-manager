"""
Class for Reservation
"""
from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Reservation(Base):
    __tablename__ = "reservation"

    reservationId = Column(Integer, primary_key=True)
    parkingId = Column(Integer, ForeignKey("parkingSpot.parkingId"))
    vehicleId = Column(Integer, ForeignKey("vehicle.vehicleId"))
    startTime = Column(Numeric(20, 0))
    endTime = Column(Numeric(20, 0))

