# from product import Product
#
# from beverage.beverage import Beverage
# from beverage.coffee import Coffee
# from beverage.hot_beverage import HotBeverage
# from beverage.cold_beverage import ColdBeverage
# from beverage.tea import Tea
#
# from food.food import Food
# from food.cake import Cake
# from food.dessert import Desert
# from food.main_dish import MainDish
# from food.salmon import Salmon
# from food.soup import Soup
# from food.starter import Starter
#
#
# # ################################################
# # Test_Code_1:
# product = Product("coffee", 2.5)
# print(product.__class__.__name__)
# print(product.name)
# print(product.price)
# beverage = Beverage("coffee", 2.5, 50)
# print(beverage.__class__.__name__)
# print(beverage.__class__.__bases__[0].__name__)
# print(beverage.name)
# print(beverage.price)
# print(beverage.milliliters)
# soup = Soup("fish soup", 9.90, 230)
# print(soup.__class__.__name__)
# print(soup.__class__.__bases__[0].__name__)
# print(soup.name)
# print(soup.price)
# print(soup.grams)
# # ------------------------------------------------
# # Output_1:
# # Product
# # coffee
# # 2.5
# # Beverage
# # Product
# # coffee
# # 2.5
# # 50
# # Soup
# # Starter
# # fish soup
# # 9.9
# # 230
# # ################################################
