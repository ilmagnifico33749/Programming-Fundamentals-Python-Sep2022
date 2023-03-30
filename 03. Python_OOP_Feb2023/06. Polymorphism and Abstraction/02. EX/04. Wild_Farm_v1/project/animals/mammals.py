# from animal import Animal
# from animal import Mammal

from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat



class Mouse(Mammal):
    def __init__(self, mouse_name: str, mouse_weight: float, mouse_living_region: str):
        super().__init__(mouse_name, mouse_weight, mouse_living_region)

    def make_sound(self):
        return f"Squeak"

    def food_animal_eats(self):
        return [Vegetable, Fruit]

    def weight_gained(self):
        return 0.10


class Dog(Mammal):
    def __init__(self, dog_name: str, dog_weight: float, dog_living_region: str):
        super().__init__(dog_name, dog_weight, dog_living_region)

    def make_sound(self):
        return f"Woof!"

    def food_animal_eats(self):
        return [Meat]

    def weight_gained(self):
        return 0.40


class Cat(Mammal):
    def __init__(self, cat_name: str, cat_weight: float, cat_living_region: str):
        super().__init__(cat_name, cat_weight, cat_living_region)

    def make_sound(self):
        return f"Meow"

    def food_animal_eats(self):
        return [Meat]

    def weight_gained(self):
        return 0.30


class Tiger(Mammal):
    def __init__(self, tiger_name: str, tiger_weight: float, tiger_living_region: str):
        super().__init__(tiger_name, tiger_weight, tiger_living_region)

    def make_sound(self):
        return f"ROAR!!!"

    def food_animal_eats(self):
        return [Meat]

    def weight_gained(self):
        return 1.00

