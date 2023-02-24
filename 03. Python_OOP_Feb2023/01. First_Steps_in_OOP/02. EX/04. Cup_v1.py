
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        quantity_to_add = quantity
        new_total_quantity = self.quantity + quantity_to_add
        if self.size >= new_total_quantity:
            self.quantity = new_total_quantity

    def status(self):
        free_space = self.size - self.quantity
        return free_space


# ############################################################
# Test_Code_1:
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
# -----------------------------------------------------------
# Output_1:
# 50
# 10
# ############################################################
