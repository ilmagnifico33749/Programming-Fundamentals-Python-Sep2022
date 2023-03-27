# from customer import Customer
# from trainer import Trainer
# from equipment import Equipment
# from exercise_plan import ExercisePlan
# from subscription import Subscription
# from typing import List

from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = list()
        self.trainers: List[Trainer] = list()
        self.equipment: List[Equipment] = list()
        self.plans: List[ExercisePlan] = list()
        self.subscriptions: List[Subscription] = list()

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, exercise_plan: ExercisePlan):
        if exercise_plan not in self.plans:
            self.plans.append(exercise_plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ""
        for subscription in self.subscriptions:
            if subscription.subscription_id == subscription_id:
                result += f"{subscription.__repr__()}\n"
                for customer in self.customers:
                    if customer.customer_id == subscription.customer_id:
                        result += f"{customer.__repr__()}\n"
                for trainer in self.trainers:
                    if trainer.trainer_id == subscription.trainer_id:
                        result += f"{trainer.__repr__()}\n"
                for exercise_plan in self.plans:
                    if exercise_plan.exercise_plan_id == subscription.exercise_id:
                        for equipment in self.equipment:
                            if equipment.equipment_id == exercise_plan.equipment_id:
                                result += f"{equipment.__repr__()}\n"
                        result += f"{exercise_plan.__repr__()}\n"

        return result
