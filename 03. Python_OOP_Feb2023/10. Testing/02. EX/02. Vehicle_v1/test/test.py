import unittest
from project.vehicle import Vehicle


class Test_Vehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 100)

    def test_default_fuel_consumption(self):
        result = self.vehicle.DEFAULT_FUEL_CONSUMPTION
        expected_result = 1.25
        self.assertEqual(result, expected_result)

    def test_init(self):
        result = [self.vehicle.fuel, self.vehicle.horse_power, self.vehicle.fuel, self.vehicle.fuel_consumption]
        expected_result = [100, 100, 100, 1.25]
        self.assertEqual(result, expected_result)

    def test_drive_not_enough_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel(self):
        self.vehicle.drive(50)
        result = self.vehicle.fuel
        expected_result = 37.5
        self.assertEqual(result, expected_result)

    def test_refuel_less_than_total_capacity(self):
        self.vehicle.drive(50)
        self.vehicle.refuel(12.5)
        result = self.vehicle.fuel
        expected_result = 50
        self.assertEqual(result, expected_result)

    def test_refuel_more_than_total_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        result = self.vehicle.__str__()
        expected_result = f"The vehicle has 100 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()


#
# class Vehicle:
#     DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
#     fuel_consumption: float
#     fuel: float
#     capacity: float
#     horse_power: float
#
#     def __init__(self, fuel: float, horse_power: float):
#         self.fuel = fuel
#         self.capacity = self.fuel
#         self.horse_power = horse_power
#         self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
#
#     def drive(self, kilometers):
#         fuel_needed = self.fuel_consumption * kilometers
#         if self.fuel < fuel_needed:
#             raise Exception("Not enough fuel")
#         self.fuel -= fuel_needed
#
#     def refuel(self, fuel):
#         if self.fuel + fuel > self.capacity:
#             raise Exception("Too much fuel")
#         self.fuel += fuel
#
#     def __str__(self):
#         return f"The vehicle has {self.horse_power} " \
#                f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
#