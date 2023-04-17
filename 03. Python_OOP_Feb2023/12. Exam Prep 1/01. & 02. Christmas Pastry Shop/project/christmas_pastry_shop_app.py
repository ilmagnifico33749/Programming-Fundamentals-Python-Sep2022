

from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    delicacy_valid_types = ["Gingerbread", "Stolen"]
    booths_valid_types = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths = list()
        self.delicacies = list()
        self.income = 0.00

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.delicacy_valid_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        elif type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.booths_valid_types:
            raise Exception(f"{type_booth} is not a valid booth!")
        if len(self.booths) > 0:
            for booth in self.booths:
                if booth.booth_number == booth_number:
                    raise Exception("Booth number {booth number} already exists!")
        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."


    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.is_reserved is False:
                if booth.capacity >= number_of_people:
                    booth.reserve(number_of_people)
                    return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")


    def order_delicacy(self, booth_number: int, delicacy_name: str):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                for delicacy in self.delicacies:
                    if delicacy.name == delicacy_name:
                        booth.delicacy_orders.append(delicacy)
                        return f"Booth {booth_number} ordered {delicacy_name}."
                raise Exception(f"No {delicacy_name} in the pastry shop!")
            raise Exception(f"Could not find booth {booth_number}!")


    def leave_booth(self, booth_number: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                income_from_booth_res = booth.price_for_reservation
                income_from_pastry_orders = sum([float(delicacy.price) for delicacy in booth.delicacy_orders])
                booth_final_bill = income_from_booth_res + income_from_pastry_orders
                self.income += booth_final_bill
                booth.delicacy_orders.clear()
                booth.price_for_reservation = 0
                booth.is_reserved = False
        return f"Booth {booth_number}:\n" \
                f"Bill: {booth_final_bill:.2f}lv."


    def get_income(self):
        return f"Income: {self.income:.2f}lv."


# ##############################################################
# Test_Code_1:
shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
# --------------------------------------------------------------
# Test_Output_1:
# Added delicacy Gingy - Gingerbread to the pastry shop.
# Gingerbread Gingy: 200g - 5.20lv.
# Added booth number 1 in the pastry shop.
# Added booth number 10 in the pastry shop.
# Booth 1 has been reserved for 30 people.
# Booth 1 ordered Gingy.
# Booth 1:
# Bill: 80.20lv.
# Booth 1 has been reserved for 5 people.
# Booth 1 ordered Gingy.
# Booth 1 ordered Gingy.
# Booth 1 ordered Gingy.
# Booth 1:
# Bill: 28.10lv.
# Income: 108.30lv.
# ##############################################################