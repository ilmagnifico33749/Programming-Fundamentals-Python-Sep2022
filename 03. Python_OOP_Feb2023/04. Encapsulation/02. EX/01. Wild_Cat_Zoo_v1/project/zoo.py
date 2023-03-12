class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            # ! animal type
            return f"{animal.name} the {animal.type} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and price > self.__budget:
            return f"Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity >= len(self.workers):
            self.workers.append(worker)
            # ! worker type
            return f"{worker.name} the {worker.type} hired successfully"

    def fire_worker(self, worker_name):
        if worker_name


