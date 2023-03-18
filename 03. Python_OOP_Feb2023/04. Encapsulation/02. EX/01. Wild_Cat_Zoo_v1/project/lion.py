from project.animal import Animal
# from animal import Animal

class Lion(Animal):
    def __init__(self, lion_name: str, lion_gender: str, lion_age: int, lion_money_for_care=50):
        super().__init__(lion_name, lion_gender, lion_age, lion_money_for_care)
