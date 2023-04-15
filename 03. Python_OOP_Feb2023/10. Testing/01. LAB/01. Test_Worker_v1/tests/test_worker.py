import unittest
from project.worker import Worker

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Michael", 5000, 100)

    def test_worker_init(self):
        result = self.worker.name, self.worker.salary, self.worker.energy
        expected_result = ("Michael", 5000, 100)
        self.assertEqual(result, expected_result)

    def test_worker_rest_method(self):
        self.worker.rest()
        result = self.worker.energy
        expected_result = 101
        self.assertEqual(result, expected_result)

    def test_error_raise_work_no_energy(self):
        with self.assertRaises(Exception):
            self.worker.energy = 0
            self.worker.work()

    def test_salary_increase_when_work_method(self):
        self.worker.work()
        result = self.worker.money
        expected_result = self.worker.salary
        self.assertEqual(result, expected_result)

    def test_energy_descrease_when_work_method(self):
        self.worker.work()
        result = self.worker.energy
        expected_result = 99
        self.assertEqual(result, expected_result)

    def test_get_info_method(self):
        result = self.worker.get_info()
        expected_result = f'Michael has saved 0 money.'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

# class Worker:
#
#     def __init__(self, name, salary, energy):
#         self.name = name
#         self.salary = salary
#         self.energy = energy
#         self.money = 0
#
#     def work(self):
#         if self.energy <= 0:
#             raise Exception('Not enough energy.')
#
#         self.money += self.salary
#         self.energy -= 1
#
#     def rest(self):
#         self.energy += 1
#
#     def get_info(self):
#         return f'{self.name} has saved {self.money} money.'



