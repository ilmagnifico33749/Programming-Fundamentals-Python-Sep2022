
class Flower:
    def __init__(self, name, water_requirements, is_happy=False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy is False:
            return f"{self.name} is not happy"
        elif self.is_happy is True:
            return f"{self.name} is happy"


# ############################################################
# Test_Code_1:
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
# -----------------------------------------------------------
# Output_1:
# Lilly is not happy
# Lilly is not happy
# Lilly is happy
# ############################################################
