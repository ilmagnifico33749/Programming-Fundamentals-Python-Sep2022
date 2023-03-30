from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def food_animal_eats(self):
        pass

    @abstractmethod
    def weight_gained(self):
        pass

    def feed(self, food):
        if food not in self.food_animal_eats():
        # attention to how the food is defined and returned
            return f"{self.__class__.__name__} does not eat {food}!"
        self.weight += self.weight_gained()
        self.food_eaten += 1

    def __repr__(self):
        pass


class Bird(Animal, ABC):
    def __init__(self, bird_name: str, bird_weight: float, bird_wing_size: float):
        self.wing_size = bird_wing_size
        super().__init__(bird_name, bird_weight)


class Mammal(Animal, ABC):
    def __init__(self, mammal_name: str, mammal_weight: float, living_region: str):
        self.living_region = living_region
        super().__init__(mammal_name, mammal_weight)

