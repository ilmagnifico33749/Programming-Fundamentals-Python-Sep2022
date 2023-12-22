from abc import ABC, abstractmethod
from project.delicacies.delicacy import Delicacy

class Stolen(Delicacy):
    def __init__(self, name: str, portion: int, price: float):
        super().__init__(name, 200, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
