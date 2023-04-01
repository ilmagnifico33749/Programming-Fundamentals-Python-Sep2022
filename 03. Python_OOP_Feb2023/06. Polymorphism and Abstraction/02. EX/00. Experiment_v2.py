# import os
# dir_list = os.listdir("C:/Users/Home PC/Documents/GitHub/SoftUni - Student/03. Python_OOP_Feb2023/06. Polymorphism and Abstraction/02. EX/04. Wild_Farm_v1")
# print(dir_list)

from project.animals.animal import Bird
from project.food import Food, Meat, Fruit, Vegetable, Seed


class Owl(Bird):
    def __init__(self, owl_name: str, owl_weight: float, owl_wing_size: float):
        super().__init__(owl_name, owl_weight, owl_wing_size)

    def make_sound(self):
        return f"Hoot Hoot"

    def food_animal_eats(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 0.25


class Hen(Bird):
    def __init__(self, hen_name: str, hen_weight: float, hen_wing_size: float):
        super().__init__(hen_name, hen_weight, hen_wing_size)

    def make_sound(self):
        return f"Cluck"

    def food_animal_eats(self):
        return [Vegetable, Fruit, Meat]

    def weight_gained(self):
        return 0.35

