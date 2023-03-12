# from project.worker import Worker
from worker import Worker

class Keeper(Worker):
    def __init__(self, keeper_name: str, keeper_age: int, keeper_salary: int):
        super().__init__(keeper_name, keeper_age, keeper_salary)
