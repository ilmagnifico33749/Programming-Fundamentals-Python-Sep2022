from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, quantity):
        ...


class Car(Vehicle):
    aircond_fuel = 0.9
    fuel_retained_refueling = 1

    def drive(self, distance):
        fuel_required = distance * (self.fuel_consumption + self.aircond_fuel)
        if fuel_required <= self.fuel_quantity:
            self.fuel_quantity -= fuel_required

    def refuel(self, quantity):
        self.fuel_quantity += quantity * self.fuel_retained_refueling


class Truck(Vehicle):
    aircond_fuel = 1.6
    fuel_retained_refueling = 0.95

    def drive(self, distance):
        fuel_required = distance * (self.fuel_consumption + self.aircond_fuel)
        if fuel_required <= self.fuel_quantity:
            self.fuel_quantity -= fuel_required

    def refuel(self, quantity):
        self.fuel_quantity += quantity * self.fuel_retained_refueling


# ##########################
# Test_Code_1:
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
# --------------------------
# Output_1:
# 2.299999999999997
# 12.299999999999997
# ##########################
# Test_Code_2:
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
# --------------------------
# Output_2:
# 17.0
# 64.5
# ##########################
