import unittest
# from project.cat import Cat


class CatTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Anubis")

    def test_cat_size_increase_when_eat(self):
        self.cat.eat()
        result = self.cat.size
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_fed_status_when_eat(self):
        self.cat.eat()
        result = self.cat.fed
        self.assertTrue(result)

    def test_raise_error_fed_when_eat(self):
        with self.assertRaises(Exception):
        # with self.assertRaises(Exception) as context:

            self.cat.eat()
            self.cat.eat()
        #  self.assertEqual(str(context.exception), 'Already fed.')

    def test_raise_error_not_fed_when_sleep(self):
        with self.assertRaises(Exception):
        # with self.assertRaises(Exception) as context:
            self.cat.sleep()
        # self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        result = self.cat.sleepy
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

# class Cat:
#
#   def __init__(self, name):
#     self.name = name
#     self.fed = False
#     self.sleepy = False
#     self.size = 0
#
#   def eat(self):
#     if self.fed:
#       raise Exception('Already fed.')
#
#     self.fed = True
#     self.sleepy = True
#     self.size += 1
#
#   def sleep(self):
#     if not self.fed:
#       raise Exception('Cannot sleep while hungry')
#
#     self.sleepy = False
