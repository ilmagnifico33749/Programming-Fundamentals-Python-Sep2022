from abc import ABC, abstractmethod
from project.food import Food, Meat, Fruit, Vegetable, Seed

class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        ...

    @abstractmethod
    def food_animal_eats(self):
        ...

    @property
    @abstractmethod
    def weight_gained(self):
        ...

    def feed(self, food):
        if food not in self.food_animal_eats():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (self.weight_gained * food.quantity)
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, bird_name: str, bird_weight: float, bird_wing_size: float):
        super().__init__(bird_name, bird_weight)
        self.wing_size = bird_wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, mammal_name: str, mammal_weight: float, living_region: str):
        super().__init__(mammal_name, mammal_weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


