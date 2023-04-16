import unittest
from project.mammal import Mammal

class Test_Mammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Fluffy", "Meerkat", "Meer")

    def test_init(self):
        result = [self.mammal.name, self.mammal.type, self.mammal.sound]
        expected_results = ["Fluffy", "Meerkat", "Meer"]
        self.assertEqual(result, expected_results)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected_results = "Fluffy makes Meer"
        self.assertEqual(result, expected_results)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_results = "animals"
        self.assertEqual(result, expected_results)

    def test_info(self):
        result = self.mammal.info()
        expected_results = "Fluffy is of type Meerkat"
        self.assertEqual(result, expected_results)


if __name__ == '__main__':
    unittest.main()


# class Mammal:
#     def __init__(self, name, mammal_type, sound):
#         self.name = name
#         self.type = mammal_type
#         self.sound = sound
#         self.__kingdom = "animals"
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def get_kingdom(self):
#         return self.__kingdom
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"
