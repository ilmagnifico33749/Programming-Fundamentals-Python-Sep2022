def shop_from_grocery_list(budget, groceries_list, *groceries_shop):
    products_bought = list()
    for product in groceries_shop:
        current_product_name = product[0]
        current_product_value = product[1]
        if current_product_name in groceries_list and current_product_name not in products_bought:
            if budget >= current_product_value:
                products_bought.append(current_product_name)
                budget -= current_product_value
            else:
                break
        else:
            pass

    if len(products_bought) == len(groceries_list):
        return (f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        return (f"You did not buy all the products. "
              f"Missing products: "
              f"{', '.join([product for product in groceries_list if product not in products_bought])}.")


# ############################################################
# Input_1:
print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
    ))
# ------------------------------------------------------------
# Output_1:
# Shopping is successful. Remaining budget: 84.20.
# ############################################################
# Input_2:
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
# ------------------------------------------------------------
# Output_2:
# You did not buy all the products. Missing products: chips.
# ############################################################
# Input_3:
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
# ------------------------------------------------------------
# Output_3:
# You did not buy all the products. Missing products: chips, meat.
# ############################################################
