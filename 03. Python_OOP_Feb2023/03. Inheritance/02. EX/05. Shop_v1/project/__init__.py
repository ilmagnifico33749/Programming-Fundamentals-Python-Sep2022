from project.product import Product
from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

# from product import Product
# from drink import Drink
# from food import Food
# from product_repository import ProductRepository

# ################################
# Test_Code_1:
food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
# ---------------------------------
# Output_1:
# [apple, water]
# water
# pple: 10
# water: 10
# ################################

