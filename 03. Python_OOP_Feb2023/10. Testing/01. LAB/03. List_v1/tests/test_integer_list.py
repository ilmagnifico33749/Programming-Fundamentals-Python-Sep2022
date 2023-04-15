import unittest
# from project.integer_list import IntegerList

class Test_integer_list(unittest.TestCase):
    def setUp(self) -> None:
        self.list_integers = IntegerList(1, 2)

    def test_add_integer(self):
        self.assertEqual(self.list_integers.add(3), [1, 2, 3])

    def test_add_not_an_integer(self):
        with self.assertRaises(ValueError):
            self.list_integers.add("not an integer")

    def test_remove_index_in_range(self):
        self.assertEqual(self.list_integers.remove_index(0), 1)

    def test_remove_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.list_integers.remove_index(3)

    def test_init_storing_input(self):
        test_list_1 = IntegerList(1, 2, 3)
        result = test_list_1.get_data()
        expected_result = [1, 2, 3]
        self.assertEqual(result, expected_result)

    def test_init_receiving_only_integers(self):
        test_list_1 = IntegerList("a", "b", "c")
        result = test_list_1.get_data()
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_get_index_existing_element(self):
        result = self.list_integers.get(0)
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_get_index_not_existing_element(self):
        with self.assertRaises(IndexError):
            invalid_index = (len(self.list_integers.get_data())+1)
            self.list_integers.get(invalid_index)

    def test_insert_valid_type_not_integer_index_in_range(self):
        self.list_integers.insert(0, 100)
        result = self.list_integers.get(0)
        expected_result = 100
        self.assertEqual(result, expected_result)

    def test_insert_invalid_type_not_integer_index_in_range(self):
        with self.assertRaises(ValueError):
            self.list_integers.insert(0, "100")

    def test_insert_valid_type_integer_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.list_integers.insert((len(self.list_integers.get_data())+1), 10)


    def test_get_biggest(self):
        result = self.list_integers.get_biggest()
        expected_result = max(self.list_integers.get_data())
        self.assertEqual(result, expected_result)

    def test_get_index_in_range(self):
        result = self.list_integers.get_index(1)
        expected_result = 0
        self.assertEqual(result, expected_result)

    # def test_get_index_out_of_range(self):
    #     with self.assertRaises(ValueError):
    #         self.list_integers.get_index(4)


if __name__ == '__main__':
    unittest.main()

