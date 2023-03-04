class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


# ######################################
# Test_Code_1:
car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
# -------------------------------------
# Output_1:
# 150
# 20
# []
# ['Hudly Wireless']
# ######################################
