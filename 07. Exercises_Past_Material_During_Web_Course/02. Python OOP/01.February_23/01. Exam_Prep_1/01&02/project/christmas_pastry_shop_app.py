from project.delicacies.delicacy import Delicacy
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    VALID_TYPES_DELICACIES = ["Gingerbread", "Stolen"]
    VALID_BOOTH_TYPES = ["Open Booth", "Private Booth"]

    def __init__(self,):
        self.booths = list()
        self.delicacies = list()
        self.income = 0.00

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in self.delicacies:
            raise Exception(f"{type_delicacy} already exists!")
        if type_delicacy not in self.VALID_TYPES_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        self.delicacies.append(type_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in self.booths:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"Added booth number {booth_number} in the pastry shop.")
        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            booth = OpenBooth(booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."


    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.is_reserved is False and booth.capacity <= number_of_people:
                booth.is_reserved = True
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
            else:
                return f"No available booth for {number_of_people} people!"

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if booth_number not in self.booths:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy_name not in self.delicacies:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        for booth in self.booths:
            if booth.booth_number == booth_number:
                booth.delicacy_orders.append(delicacy_name)
                return f"Booth {booth_number} ordered {delicacy_name}."



    def leave_booth(self, booth_number: int):
        pass

    @staticmethod
    def get_income():
        pass
