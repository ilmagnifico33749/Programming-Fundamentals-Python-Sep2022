from project.worker import Worker
# from worker import Worker

class Vet(Worker):
    def __init__(self, vet_name: str, vet_age: int, vet_salary: int):
        super().__init__(vet_name, vet_age, vet_salary)
