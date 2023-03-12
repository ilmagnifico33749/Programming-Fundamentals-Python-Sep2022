# from project.animal import Animal
from animal import Animal

class Tiger(Animal):
    def __init__(self, tiger_name: str, tiger_gender: str, tiger_age: int, tiger_money_for_care=45):
        super().__init__(tiger_name, tiger_gender, tiger_age, tiger_money_for_care)
