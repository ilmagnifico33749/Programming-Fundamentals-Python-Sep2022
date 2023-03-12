# from project.animal import Animal
from animal import Animal

class Cheetah(Animal):
    def __init__(self, cheetah_name: str, cheetah_gender: str, cheetah_age: int, cheetah_money_for_care=60):
        super().__init__(cheetah_name, cheetah_gender, cheetah_age, cheetah_money_for_care)
