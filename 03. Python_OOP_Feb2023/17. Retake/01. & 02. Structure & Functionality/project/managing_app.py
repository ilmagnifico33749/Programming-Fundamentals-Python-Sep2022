import operator
from collections import deque

from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan
from project.user import User
from project.route import Route


class ManagingApp:
    vehicles_valid_types = ["PassengerCar", "CargoVan"]

    def __init__(self):
        self.users = list()
        self.vehicles = list()
        self.routes = list()

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self.users:
            for user in self.users:
                if user.driving_license_number == driving_license_number:
                    return f"{driving_license_number} has already been registered to our platform."
        current_user = User(first_name, last_name, driving_license_number)
        self.users.append(current_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        current_vehicle = ...
        if vehicle_type not in self.vehicles_valid_types:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if self.vehicles:
            for vehicle in self.vehicles:
                if vehicle.license_plate_number == license_plate_number:
                    return f"{license_plate_number} belongs to another vehicle."
        if vehicle_type == "PassengerCar":
            current_vehicle = PassengerCar(brand, model, license_plate_number)
        elif vehicle_type == "CargoVan":
            current_vehicle = CargoVan(brand, model, license_plate_number)
        self.vehicles.append(current_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        current_route_id = (len(self.routes) + 1)
        current_route = Route(start_point, end_point, length, current_route_id)
        if self.routes:
            for route in self.routes:
                if route.start_point == start_point and route.end_point == end_point and route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.start_point == start_point and route.end_point == end_point and route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.start_point == start_point and route.end_point == end_point and route.length > length:
                    route.is_locked = True
        self.routes.append(current_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        current_user = ...
        current_vehicle = ...
        current_route = ...

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                current_user = user
                if user.is_blocked is True:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                current_vehicle = vehicle
                if vehicle.is_damaged is True:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        for route in self.routes:
            if route.route_id == route_id:
                current_route = route
                if route.is_locked is True:
                    return f"Route {route_id} is locked! This trip is not allowed."


        current_vehicle.drive(current_route.length)
        if is_accident_happened:
            current_vehicle.is_damaged = True
            current_user.decrease_rating()
        else:
            current_user.increase_rating()

        return current_vehicle.__str__()


    def repair_vehicles(self, count: int):
        count_of_repaired_vehicles = 0
        vehicles_to_be_repaired = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged is True:
                vehicles_to_be_repaired.append(vehicle)
        sorted_list = deque(sorted(vehicles_to_be_repaired, key=operator.attrgetter("brand", "model")))

        if count <= len(sorted_list):
            for repairs in range(count):
                current_car_to_repair = sorted_list.popleft()
                for car in self.vehicles:
                    if car == current_car_to_repair:
                        car.is_damaged = False
                        car.recharge()
                        count_of_repaired_vehicles += 1
        elif count > len(sorted_list):
            for current_car_to_repair in sorted_list:
                for car in self.vehicles:
                    if car == current_car_to_repair:
                        car.is_damaged = False
                        car.recharge()
                        count_of_repaired_vehicles += 1

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"


    def users_report(self):
        result = "*** E-Drive-Rent ***"
        sorted_list = sorted(self.users, key=operator.attrgetter("rating"), reverse=True)
        for user in sorted_list:
            result += f"\n{user}"
        return result


# ###########################################################################
# Test_Code_1:
app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
# ---------------------------------------------------------------------------
# Output_1:
# Tisha Reenie was successfully registered under DLN-7246506
# Bernard Remy was successfully registered under DLN-CDYHVSR68661
# 7246506 has already been registered to our platform.
# Chevrolet Volt was successfully uploaded with LPN-CWP8032.
# Volkswagen e-Up! was successfully uploaded with LPN-COUN199728.
# Mercedes-Benz EQS was successfully uploaded with LPN-5UNM315.
# Ford e-Transit was successfully uploaded with LPN-726QOA.
# BrightDrop Zevo400 was successfully uploaded with LPN-SC39690.
# Vehicle type EcoTruck is inaccessible.
# 726QOA belongs to another vehicle.
# SOF/PLD - 144 km is unlocked and available to use.
# BUR/VAR - 87 km is unlocked and available to use.
# BUR/VAR - 87 km had already been added to our platform.
# SOF/PLD shorter route had already been added to our platform.
# BUR/VAR - 86.999 km is unlocked and available to use.
# Mercedes-Benz EQS License plate: 5UNM315 Battery: 81% Status: OK
# Chevrolet Volt License plate: CWP8032 Battery: 68% Status: Damaged
# User 7246506 is blocked in the platform! This trip is not allowed.
# Vehicle CWP8032 is damaged! This trip is not allowed.
# Route 2 is locked! This trip is not allowed.
# 1 vehicles were successfully repaired!
# 0 vehicles were successfully repaired!
# *** E-Drive-Rent ***
# Bernard Remy Driving license: CDYHVSR68661 Rating: 0.5
# Tisha Reenie Driving license: 7246506 Rating: 0
# ###########################################################################







