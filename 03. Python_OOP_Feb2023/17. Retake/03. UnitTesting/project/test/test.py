# 100/100

import unittest
from project.robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot("TestID", "Humanoids", 20, 1000.00)

    def test_init_valid_input(self):
        result = [self.robot.robot_id, self.robot.category, self.robot.available_capacity, self.robot.price]
        expected_result = ["TestID", "Humanoids", 20, 1000.00]
        self.assertEqual(result, expected_result)

    def test_init_invalid_category_input(self):
        with self.assertRaises(ValueError) as exp_msg:
            current_test_robot = Robot("TestID", "Invalid_Category", 20, 1000.00)
        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(exp_msg.exception))

    def test_init_invalid_price_input(self):
        with self.assertRaises(ValueError) as exp_msg:
            current_test_robot = Robot("TestID", "Humanoids", 20, -10.00)
        self.assertEqual(f"Price cannot be negative!", str(exp_msg.exception))


    def test_upgrade_valid_input(self):
        result = self.robot.upgrade("Test_Component", 500)
        expected_result = f"Robot TestID was upgraded with Test_Component."
        self.assertEqual(result, expected_result)

    def test_upgrade_valid_input_calculations(self):
        self.robot.upgrade("Test_Component", 500)
        result_hardware_upgrades = self.robot.hardware_upgrades
        expected_result_hardware_upgrades = ["Test_Component"]
        result_price_increase = self.robot.price
        expected_result_price_increase = 1750.0
        self.assertEqual(result_hardware_upgrades, expected_result_hardware_upgrades)
        self.assertEqual(result_price_increase, expected_result_price_increase)

    def test_upgrade_invalid_input(self):
        self.robot.upgrade("Test_Component", 500)
        result = self.robot.upgrade("Test_Component", 500)
        expected_result = f"Robot TestID was not upgraded."
        self.assertEqual(result, expected_result)


    def test_update_valid_input(self):
        result = self.robot.update(10.0, 20)
        expected_result = f'Robot TestID was updated to version 10.0.'
        self.assertEqual(result, expected_result)

    def test_update_valid_input_calculations(self):
        self.robot.update(10.0, 20)
        result_software_updates = self.robot.software_updates
        expected_result_software_updates = [10.0]
        result_available_capacity = self.robot.available_capacity
        expected_available_capacity = 0
        self.assertEqual(result_software_updates, expected_result_software_updates)
        self.assertEqual(result_available_capacity, expected_available_capacity)

    def test_update_invalid_input_previous_version(self):
        self.robot.update(10.0, 10)
        result = self.robot.update(9.0, 5)
        expected_result = f"Robot TestID was not updated."
        self.assertEqual(result, expected_result)

    def test_update_invalid_insufficient_capacity(self):
        self.robot.update(10.0, 15)
        result = self.robot.update(11.0, 30)
        expected_result = f"Robot TestID was not updated."
        self.assertEqual(result, expected_result)


    def test_gt_comparison_higher_price(self):
        robot_one = Robot("TestID1", "Humanoids", 20, 1500.00)
        robot_two = Robot("TestID2", "Humanoids", 20, 1000.00)
        result = robot_one.__gt__(robot_two)
        expected_result = f'Robot with ID TestID1 is more expensive than Robot with ID TestID2.'
        self.assertEqual(result, expected_result)

    def test_gt_comparison_equal_price(self):
        robot_one = Robot("TestID1", "Humanoids", 20, 1000.00)
        robot_two = Robot("TestID2", "Humanoids", 20, 1000.00)
        result = robot_one.__gt__(robot_two)
        expected_result = f'Robot with ID TestID1 costs equal to Robot with ID TestID2.'
        self.assertEqual(result, expected_result)

    def test_gt_comparison_lower_price(self):
        robot_one = Robot("TestID1", "Humanoids", 20, 1000.00)
        robot_two = Robot("TestID2", "Humanoids", 20, 1500.00)
        result = robot_one.__gt__(robot_two)
        expected_result = f'Robot with ID TestID1 is cheaper than Robot with ID TestID2.'
        self.assertEqual(result, expected_result)


    def test_ALLOWED_CATEGORIES(self):
        result = self.robot.ALLOWED_CATEGORIES
        expected_result = ['Military', 'Education', 'Entertainment', 'Humanoids']
        self.assertEqual(result, expected_result)

    def test_PRICE_INCREMENT(self):
        result = self.robot.PRICE_INCREMENT
        expected_result = 1.5
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
