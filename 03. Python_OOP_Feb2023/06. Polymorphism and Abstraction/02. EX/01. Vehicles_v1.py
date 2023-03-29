# ! 83/100 in Judge - 1 X from 6 /the second one/

from abc import ABC, abstractmethod, abstractclassmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        # The fuel consumption is per km.
        self.fuel_consumption = fuel_consumption
        super().__init__()
        
    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self.__fuel_consumption = (value + 0.9)

    @property
    def fuel_quantity(self):
        return self.__fuel_quantity

    @fuel_quantity.setter
    def fuel_quantity(self, value):
        self.__fuel_quantity = value

    def drive(self, distance):
        fuel_spent = distance * self.__fuel_consumption
        if self.__fuel_quantity >= fuel_spent:
            self.__fuel_quantity -= fuel_spent

    def refuel(self, fuel):
        self.__fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        # The fuel consumption is per km.
        self.fuel_consumption = fuel_consumption
        super().__init__()

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self.__fuel_consumption = (value + 1.6)

    @property
    def fuel_quantity(self):
        return self.__fuel_quantity

    @fuel_quantity.setter
    def fuel_quantity(self, value):
        self.__fuel_quantity = value

    def drive(self, distance):
        fuel_spent = distance * self.__fuel_consumption
        if self.__fuel_quantity >= fuel_spent:
            self.__fuel_quantity -= fuel_spent

    def refuel(self, fuel):
        self.__fuel_quantity += (fuel * 0.95)


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
