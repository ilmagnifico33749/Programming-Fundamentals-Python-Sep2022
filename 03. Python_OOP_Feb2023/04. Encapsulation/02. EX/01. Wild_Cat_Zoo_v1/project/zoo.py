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
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and price > self.__budget:
            return f"Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for specific_worker in self.workers:
            if specific_worker.name == worker_name:
                self.workers.remove(specific_worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        budget_required_all = 0
        for current_worker in self.workers:
            budget_required_all += current_worker.salary
        if self.__budget < budget_required_all:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= budget_required_all
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        budget_required_all = 0
        for current_animal in self.animals:
            budget_required_all += current_animal.money_for_care
        if self.__budget < budget_required_all:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= budget_required_all
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        list_lions = [current_animal for current_animal in self.animals if current_animal.__class__.__name__ == "Lion"]
        list_tigers = [current_animal for current_animal in self.animals if current_animal.__class__.__name__ == "Tiger"]
        list_cheetahs = [current_animal for current_animal in self.animals if current_animal.__class__.__name__ == "Cheetah"]

        lions_info = '\n'.join([str(current_lion) for current_lion in list_lions])
        tigers_info = '\n'.join([str(current_tiger) for current_tiger in list_tigers])
        cheetahs_info = '\n'.join([str(current_cheetah) for current_cheetah in list_cheetahs])

        result = [f"You have {len(self.animals)} animals",
                  f"----- {len(list_lions)} Lions:", lions_info,
                  f"----- {len(list_tigers)} Tigers:", tigers_info,
                  f"----- {len(list_cheetahs)} Cheetahs:", cheetahs_info]

        return '\n'.join(result)

    def workers_status(self):
        list_keepers = [current_worker for current_worker in self.workers if current_worker.__class__.__name__ == "Keeper"]
        list_caretakers = [current_worker for current_worker in self.workers if current_worker.__class__.__name__ == "Caretaker"]
        list_vets = [current_worker for current_worker in self.workers if current_worker.__class__.__name__ == "Vet"]

        keepers_info = '\n'.join([str(current_keeper) for current_keeper in list_keepers])
        caretakers_info = '\n'.join([str(current_caretaker) for current_caretaker in list_caretakers])
        vets_info = '\n'.join([str(current_vet) for current_vet in list_vets])

        result = [f"You have {len(self.workers)} workers",
                  f"----- {len(list_keepers)} Keepers:", keepers_info,
                  f"----- {len(list_caretakers)} Caretakers:", caretakers_info,
                  f"----- {len(list_vets)} Vets:", vets_info]

        return '\n'.join(result)




