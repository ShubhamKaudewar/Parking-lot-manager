# Parking Lot Management System API

## Problem Statement

You are required to build a **Parking Lot Management System API** that allows users to manage parking spots, vehicles, and reservations. The system should include CRUD (Create, Read, Update, Delete) operations for managing parking spots and tracking vehicle reservations.

## Entities

### Parking Spot

- **ID**: Primary Key (Auto-incremented)
- **Spot Number**: Integer
- **Status**: Available, Occupied, Maintenance (String)
- **Vehicle Type**: Small, Medium, Large (String)

### Vehicle

- **ID**: Primary Key (Auto-incremented)
- **License Plate**: String
- **Vehicle Type**: Small, Medium, Large (String)
- **Owner Name**: String

### Reservation

- **ID**: Primary Key (Auto-incremented)
- **Parking Spot ID**: Foreign Key (References Parking Spot)
- **Vehicle ID**: Foreign Key (References Vehicle)
- **Start Time**: Numeric (Unix timestamp)
- **End Time**: Numeric (Unix timestamp)

## Endpoints

### Parking Spot CRUD

- **Create Parking Spot**: `POST /parking-spot/`
- **Get All Parking Spots**: `GET /parking-spot/`
- **Get Parking Spot by ID**: `GET /parking-spot/{id}`
- **Update Parking Spot**: `PUT /parking-spot/{id}`
- **Delete Parking Spot**: `DELETE /parking-spot/{id}`

### Vehicle CRUD

- **Create Vehicle**: `POST /vehicle/`
- **Get All Vehicles**: `GET /vehicle/`
- **Get Vehicle by ID**: `GET /vehicle/{id}`
- **Update Vehicle**: `PUT /vehicle/{id}`
- **Delete Vehicle**: `DELETE /vehicle/{id}`

### Reservation CRUD

- **Create Reservation**: `POST /reservation/`
- **Get All Reservations**: `GET /reservation/`
- **Get Reservation by ID**: `GET /reservation/{id}`
- **Update Reservation**: `PUT /reservation/{id}`
- **Delete Reservation**: `DELETE /reservation/{id}`

## Additional Endpoints

- **Get Available Parking Spots**: `GET /parking-spot/available`
- **Check Parking Spot Status**: `GET /parking-spot/{id}/status`

## Usage

This API allows you to:
- **Manage Parking Spots**: Create, update, delete, and retrieve parking spots.
- **Manage Vehicles**: Add vehicles, update details, and remove them from the system.
- **Handle Reservations**: Reserve parking spots for specific vehicles, update reservation times, or cancel reservations.
- **Monitor Parking Spot Availability**: Get a list of available spots and check the status of individual spots.

## Technologies

- **API Framework**: FastAPI (or Flask/Django if preferred)
- **Database**: SQLite, PostgreSQL, or MySQL
- **Authentication**: JWT (optional for advanced security)

Feel free to clone the repo and modify it to fit your specific parking management requirements!
