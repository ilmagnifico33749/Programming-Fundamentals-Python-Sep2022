import unittest
from project.toy_store import ToyStore

class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.MyToyStore = ToyStore()

    def test_store_shelves_init(self):
        result = self.MyToyStore.toy_shelf
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(result, expected_result)

    def test_add_toy_shelf_not_exist(self):
        with self.assertRaises(Exception) as context:
            result = self.MyToyStore.add_toy("Z", "Train")
        expected_message = "Shelf doesn't exist!"
        self.assertEqual(str(context.exception), expected_message)

    def test_add_toy_already_in_shelf(self):
        with self.assertRaises(Exception) as context:
            self.MyToyStore.add_toy("E", "train")
            result = self.MyToyStore.add_toy("E", "train")
        expected_message = "Toy is already in shelf!"
        self.assertEqual(str(context.exception), expected_message)

    def test_add_toy_shelf_already_taken(self):
        with self.assertRaises(Exception) as context:
            self.MyToyStore.add_toy("E", "train")
            result = self.MyToyStore.add_toy("E", "Andy")
        expected_message = "Shelf is already taken!"
        self.assertEqual(str(context.exception), expected_message)

    def test_add_toy_success(self):
        shelf = "E"
        toy_name = "train"

        result_message = self.MyToyStore.add_toy(shelf, toy_name)
        expected_message = "Toy:train placed successfully!"
        self.assertEqual(result_message, expected_message)
        self.assertEqual(self.MyToyStore.toy_shelf[shelf], toy_name)

    def test_remove_toy_shelf_not_exist(self):
        with self.assertRaises(Exception) as context:
            result = self.MyToyStore.remove_toy("Z", "train")
        expected_message = "Shelf doesn't exist!"
        self.assertEqual(str(context.exception), expected_message)

    def test_remove_toy_toy_not_in_shelf(self):
        with self.assertRaises(Exception) as context:
            result = self.MyToyStore.remove_toy("E", "train")
        expected_message = "Toy in that shelf doesn't exists!"
        self.assertEqual(str(context.exception), expected_message)

    def test_remove_toy_success(self):
        shelf = "E"
        toy_name = "train"
        self.MyToyStore.add_toy(shelf, toy_name)
        result_message = self.MyToyStore.remove_toy(shelf, toy_name)
        expected_message = "Remove toy:train successfully!"
        self.assertEqual(result_message, expected_message)
        self.assertEqual(self.MyToyStore.toy_shelf["E"], None)




if __name__ == '__main__':
    unittest.main()


