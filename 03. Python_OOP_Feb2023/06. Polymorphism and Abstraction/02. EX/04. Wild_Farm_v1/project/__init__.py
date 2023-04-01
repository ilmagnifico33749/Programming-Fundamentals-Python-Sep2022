from project.food import Food, Vegetable, Fruit, Meat, Seed
from animals.animal import Animal, Bird, Mammal
from animals.birds import Owl, Hen
from animals.mammals import Mouse, Dog, Cat, Tiger



# ############################
# Test_Code_1:
owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
print(50 * "#")
# ----------------------------
# Output_1:
# Owl [Pip, 10, 10, 0]
# Hoot Hoot
# Owl does not eat Vegetable!
# Owl [Pip, 10, 11.0, 4]
# ############################
# Test_Code_2:
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
print(50 * "#")

# ----------------------------
# Output_2:
# Hen [Harry, 10, 10, 0]
# Cluc
# Hen [Harry, 10, 13.15, 9
# ############################
