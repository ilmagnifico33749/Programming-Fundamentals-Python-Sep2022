import unittest
# from project.car_manager import Car

class Test_Car(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Audi", "R8", 7, 100)
    # def __init__(self, make, model, fuel_consumption, fuel_capacity):

    def test_make_value_entered(self):
        result = self.car.make
        expected_result = "Audi"
        self.assertEqual(result, expected_result)

    def test_make_value_not_entered(self):
        with self.assertRaises(Exception):
            test_car = Car(None, "R8", 7, 100)

    def test_model_value_entered(self):
        result = self.car.model
        expected_result = "R8"
        self.assertEqual(result, expected_result)

    def test_model_value_not_entered(self):
        with self.assertRaises(Exception):
            test_car = Car("Audi", None, 7, 100)

    def test_fuel_consumption_value_valid(self):
        result = self.car.fuel_consumption
        expected_result = 7
        self.assertEqual(result, expected_result)

    def test_fuel_consumption_value_not_valid(self):
        with self.assertRaises(Exception):
            test_car = Car("Audi", "r8", 0, 100)

    def test_fuel_capacity_value_valid(self):
        result = self.car.fuel_capacity
        expected_result = 100
        self.assertEqual(result, expected_result)

    def test_fuel_capacity_value_not_valid(self):
        with self.assertRaises(Exception):
            test_car = Car("Audi", "r8", 7, 0)

    def test_fuel_amount_value_valid(self):
        result = self.car.fuel_amount
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_fuel_amount_value_not_valid(self):
        with self.assertRaises(Exception):
            self.car.fuel_amount = -1

    def test_refuel_value_invalid(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_refuel_amount_less_then_capacity(self):
        self.car.refuel(50)
        result = self.car.fuel_amount
        expected_result = 50
        self.assertEqual(result, expected_result)

    def test_refuel_amount_higher_then_capacity(self):
        self.car.refuel(200)
        result = self.car.fuel_amount
        expected_result = 100
        self.assertEqual(result, expected_result)

    def test_drive_fuel_needed_more_than_is_available(self):
        with self.assertRaises(Exception):
            self.car.drive(1000000)

    def test_drive_fuel_needed_less_or_equal_than_is_available(self):
        self.car.refuel(15)
        self.car.drive(100)
        result = self.car.fuel_amount
        expected_result = 8
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
