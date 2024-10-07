"""
Class for Vehicle
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Vehicle(Base):
    __tablename__ = "vehicle"

    vehicleId = Column(Integer, primary_key=True)
    licencePlate = Column(String(255))
    vehicleType = Column(String(255))
    ownerName = Column(String(255))

    # relationship
    reservation = relationship("Reservation", backref="vehicle")
