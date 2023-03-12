# from project.worker import Worker
from worker import Worker

class Caretaker(Worker):
    def __init__(self, caretaker_name: str, caretaker_age: int, caretaker_salary: int):
        super().__init__(caretaker_name, caretaker_age, caretaker_salary)
