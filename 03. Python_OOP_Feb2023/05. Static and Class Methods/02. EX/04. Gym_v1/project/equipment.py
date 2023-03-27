class Equipment:
    equipment_id = 1

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_next_id():
        next_equipment_id = Equipment.customer_id + 1
        return next_equipment_id

    def __repr__(self):
        return f"Equipment <{self.equipment_id}> {self.name}"
