from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if int(value) < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        earnings_from_race = 0
        for sponsor, rewards_dict in self.sponsors.items():
            for position, reward in rewards_dict.items():
                if race_pos <= position:
                    earnings_from_race += reward
                    break

        revenue = earnings_from_race - self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

