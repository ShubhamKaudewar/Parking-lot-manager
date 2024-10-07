"""
Class for Parking Spot
"""

from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
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


class Vehicle(Base):
    __tablename__ = "vehicle"

    vehicleId = Column(Integer, primary_key=True)
    licensePlate = Column(String(255))
    vehicleType = Column(String(255))
    ownerName = Column(String(255))

    # relationship
    reservation = relationship("Reservation", backref="vehicle")


class Reservation(Base):
    __tablename__ = "reservation"

    reservationId = Column(Integer, primary_key=True)
    parkingId = Column(Integer, ForeignKey("parkingSpot.parkingId"))
    vehicleId = Column(Integer, ForeignKey("vehicle.vehicleId"))
    startTime = Column(Numeric(20, 0))
    endTime = Column(Numeric(20, 0))
