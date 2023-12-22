from abc import ABC, abstractmethod
from project.delicacies.delicacy import Delicacy



class Gingerbread(Delicacy):
    def __init__(self, name: str, portion: int, price: float):
        super().__init__(name, 250, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."















