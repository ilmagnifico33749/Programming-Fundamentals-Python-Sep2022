from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, vegetable_quantity):
        super().__init__(vegetable_quantity)


class Fruit(Food):
    def __init__(self, fruit_quantity):
        super().__init__(fruit_quantity)


class Meat(Food):
    def __init__(self, meat_quantity):
        super().__init__(meat_quantity)


class Seed(Food):
    def __init__(self, seed_quantity):
        super().__init__(seed_quantity)


