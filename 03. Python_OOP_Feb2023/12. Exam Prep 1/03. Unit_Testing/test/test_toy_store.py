# 100/100

import unittest
from project.toy_store import ToyStore

class Test_Toy_Store(unittest.TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_init_no_input(self):
        result = self.toy_store.toy_shelf
        expected_result = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(result, expected_result)
############################
    def test_add_toy_valid_input(self):
        result = self.toy_store.add_toy("A", "Constructor")
        expected_result = f"Toy:Constructor placed successfully!"
        self.assertEqual(result, expected_result)

    def test_add_toy_toy_already_in_shelf(self):
        with self.assertRaises(Exception) as exp_msg:
            self.toy_store.add_toy("A", "Constructor")
            self.toy_store.add_toy("A", "Constructor")
        self.assertEqual("Toy is already in shelf!", str(exp_msg.exception))

    def test_add_toy_data_update(self):
        self.toy_store.add_toy("A", "Constructor")
        result = self.toy_store.toy_shelf
        expected_result = {"A": "Constructor", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(result, expected_result)

    def test_add_toy_shelf_value_not_none(self):
        with self.assertRaises(Exception) as exp_msg:
            self.toy_store.add_toy("A", "Ball")
            self.toy_store.add_toy("A", "Constructor")
        self.assertEqual("Shelf is already taken!", str(exp_msg.exception))

    def test_add_toy_shelf_not_existing(self):
        with self.assertRaises(Exception) as exp_msg:
            self.toy_store.add_toy("Z", "Constructor")
        self.assertEqual("Shelf doesn't exist!", str(exp_msg.exception))
################################
    def test_remove_toy_valid_input(self):
        self.toy_store.add_toy("A", "Constructor")
        result = self.toy_store.remove_toy("A", "Constructor")
        expected_result = f"Remove toy:Constructor successfully!"
        self.assertEqual(result, expected_result)

    def test_remove_toy_shelf_not_existing(self):
        with self.assertRaises(Exception) as exp_msg:
            self.toy_store.remove_toy("Z", "Constructor")
        self.assertEqual("Shelf doesn't exist!", str(exp_msg.exception))

    def test_remove_toy_toy_not_in_shelf(self):
        with self.assertRaises(Exception) as exp_msg:
            self.toy_store.remove_toy("A", "Constructor")
        self.assertEqual("Toy in that shelf doesn't exists!", str(exp_msg.exception))

    def test_remove_toy_data_update(self):
        self.toy_store.add_toy("A", "Constructor")
        self.toy_store.remove_toy("A", "Constructor")
        result = self.toy_store.toy_shelf
        expected_result = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(result, expected_result)
################################

if __name__ == "__main__":
    unittest.main()

#
# class ToyStore:
#     def __init__(self):
#         self.toy_shelf = {
#             "A": None,
#             "B": None,
#             "C": None,
#             "D": None,
#             "E": None,
#             "F": None,
#             "G": None,
#         }
#
#     def add_toy(self, shelf: str, toy_name: str):
#         if shelf not in self.toy_shelf.keys():
#             raise Exception("Shelf doesn't exist!")
#         if self.toy_shelf[shelf] == toy_name:
#             raise Exception("Toy is already in shelf!")
#         if self.toy_shelf[shelf] is not None:
#             raise Exception("Shelf is already taken!")
#         self.toy_shelf[shelf] = toy_name
#         return f"Toy:{toy_name} placed successfully!"
#
#     def remove_toy(self, shelf: str, toy_name: str):
#         if shelf not in self.toy_shelf.keys():
#             raise Exception("Shelf doesn't exist!")
#         if self.toy_shelf[shelf] != toy_name:
#             raise Exception("Toy in that shelf doesn't exists!")
#         self.toy_shelf[shelf] = None
#         return f"Remove toy:{toy_name} successfully!"