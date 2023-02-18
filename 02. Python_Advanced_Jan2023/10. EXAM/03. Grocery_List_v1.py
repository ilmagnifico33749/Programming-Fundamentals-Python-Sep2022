# Couldn't submit it, Judge bugged ... although I should've gotten 100/100
from collections import deque

def shop_from_grocery_list(budget, shopping_list, *groceries_tuple):
    budget = int(budget)
    shopping_list = shopping_list
    groceries_tuple = deque(groceries_tuple)
    budget_enough = True
    current_product_info = groceries_tuple[0]
    product_name = current_product_info[0]
    product_price = current_product_info[1]

    if product_name in shopping_list:
        if budget >= product_price:
            shopping_list.remove(product_name)
            groceries_tuple.popleft()
            budget -= product_price
        elif budget < product_price:
            budget_enough = False

    if len(shopping_list) > 0 and len(groceries_tuple) > 0 and budget_enough is True:
        return shop_from_grocery_list(budget, shopping_list, *groceries_tuple)
    else:
        if len(shopping_list) == 0 or len(groceries_tuple) > 0 and budget_enough == True:
            return f"Shopping is successful. Remaining budget: {budget}"
        elif len(groceries_tuple) == 0:
            return f"You did not buy all the products. Missing products: {', '.join(x for x in shopping_list)}"
        elif budget_enough == False:
            return f"You did not buy all the products. Missing products: {', '.join(x for x in shopping_list)}"


# ############################################################
# Input_1:
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
#     ))
# ------------------------------------------------------------
# Output_1:
# Shopping is successful. Remaining budget: 84.20.
# ############################################################
# Input_2:
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
# ------------------------------------------------------------
# Output_2:
# You did not buy all the products. Missing products: chips.
# ############################################################
# Input_3:
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
# ------------------------------------------------------------
# Output_3:
# You did not buy all the products. Missing products: chips, meat.
# ############################################################
