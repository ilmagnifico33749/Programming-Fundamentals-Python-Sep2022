import unittest
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.MyClimbingRobot = ClimbingRobot("Mountain", "PartType", 100, 1000)

    def test_init(self):
        result = [self.MyClimbingRobot.category, self.MyClimbingRobot.part_type, self.MyClimbingRobot.capacity, self.MyClimbingRobot.memory, self.MyClimbingRobot.installed_software]
        expected_result = ["Mountain", "PartType", 100, 1000, []]
        self.assertEqual(result, expected_result)

    def test_category_setter_error(self):
        with self.assertRaises(ValueError) as context:
            self.MyClimbingRobot.category = "InvalidCategory"
        expected_message = (f"Category should be one of {self.MyClimbingRobot.ALLOWED_CATEGORIES}")
        self.assertEqual(str(context.exception), expected_message)

    def test_category_setter_success(self):
        self.MyClimbingRobot.category = "Alpine"
        result = self.MyClimbingRobot.category
        expected_result = "Alpine"
        self.assertEqual(result, expected_result)

    def test_get_used_capacity(self):
        result = self.MyClimbingRobot.get_used_capacity()
        expected_result = 0
        self.assertEqual(result, expected_result)
        software = {'name': 'Update', 'capacity_consumption': 50, 'memory_consumption': 500}
        self.MyClimbingRobot.install_software(software)
        second_result =self.MyClimbingRobot.get_used_capacity()
        second_expected_result = 50
        self.assertEqual(second_result, second_expected_result)


    def test_get_available_capacity(self):
        result = self.MyClimbingRobot.get_available_capacity()
        expected_result = 100
        self.assertEqual(result, expected_result)
        software = {'name': 'Update', 'capacity_consumption': 50, 'memory_consumption': 500}
        self.MyClimbingRobot.install_software(software)
        second_result = self.MyClimbingRobot.get_available_capacity()
        second_expected_result = 50
        self.assertEqual(second_result, second_expected_result)

    def test_get_used_memory(self):
        result = self.MyClimbingRobot.get_used_memory()
        expected_result = 0
        self.assertEqual(result, expected_result)
        software = {'name': 'Update', 'capacity_consumption': 50, 'memory_consumption': 500}
        self.MyClimbingRobot.install_software(software)
        second_result = self.MyClimbingRobot.get_used_memory()
        second_expected_result = 500
        self.assertEqual(second_result, second_expected_result)


    def test_get_available_memory(self):
        result = self.MyClimbingRobot.get_available_memory()
        expected_result = 1000
        self.assertEqual(result, expected_result)
        software = {'name': 'Update', 'capacity_consumption': 50, 'memory_consumption': 500}
        self.MyClimbingRobot.install_software(software)
        second_result = self.MyClimbingRobot.get_available_memory()
        second_expected_result = 500
        self.assertEqual(second_result, second_expected_result)

    def test_install_software_success(self):
        software_one = {'name': 'Update1', 'capacity_consumption': 50, 'memory_consumption': 250}
        software_two = {'name': 'Update2', 'capacity_consumption': 50, 'memory_consumption': 250}
        result_one = self.MyClimbingRobot.install_software(software_one)
        expected_message_one = f"Software '{software_one['name']}' successfully installed on Mountain part."
        self.assertEqual(result_one, expected_message_one)
        self.assertEqual(self.MyClimbingRobot.installed_software, [software_one])
        result_two = self.MyClimbingRobot.install_software(software_two)
        expected_message_two = f"Software '{software_two['name']}' successfully installed on Mountain part."
        self.assertEqual(result_two, expected_message_two)
        self.assertEqual(self.MyClimbingRobot.installed_software, [software_one, software_two])


    def test_install_software_error(self):
        software = {'name': 'Update', 'capacity_consumption': 100, 'memory_consumption': 1500}
        result = self.MyClimbingRobot.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on Mountain part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.MyClimbingRobot.installed_software, [])

if __name__ == '__main__':
    unittest.main()
