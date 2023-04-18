from project.vehicles.base_vehicle import BaseVehicle

class PassengerCar(BaseVehicle):
    max_mileage = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.max_mileage)

    def drive(self, mileage: float):
        mileage_percentage_max_mileage = self.max_mileage / mileage
        self.battery_level -= int(self.battery_level / mileage_percentage_max_mileage)

