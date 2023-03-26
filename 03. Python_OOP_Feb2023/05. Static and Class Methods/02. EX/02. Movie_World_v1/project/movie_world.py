from typing import List

# from customer import Customer
# from dvd import DVD

from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if current_dvd.is_rented is True:
            if current_dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {current_dvd.name}"
            return f"DVD is already rented"

        if current_dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        customer.rented_dvds.append(current_dvd)
        return f"{customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if current_dvd in customer.rented_dvds:
            customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{customer.name} has successfully returned {current_dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""

        for customer in self.customers:
            result += f"{customer.__repr__()}\n"

        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"

        return result




