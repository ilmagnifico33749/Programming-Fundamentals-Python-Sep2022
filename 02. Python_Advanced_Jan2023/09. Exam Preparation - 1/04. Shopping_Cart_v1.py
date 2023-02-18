
def dict_verif_modif(current_meal, current_product, dict):
    dictionary = dict
    if current_product not in dictionary[current_meal]:
        if current_meal == "Soup":
            if len(dictionary[current_meal]) < 3:
                dictionary[current_meal].append(current_product)
        if current_meal == "Pizza":
            if len(dictionary[current_meal]) < 4:
                dictionary[current_meal].append(current_product)
        if current_meal == "Desert":
            if len(dictionary[current_meal]) < 2:
                dictionary[current_meal].append(current_product)
    return dictionary


def shopping_cart(*args):
    dict_shopping_cart = {'Pizza': [], 'Soup': [], 'Dessert': []}
    for sublist in args:
        if sublist != "Stop":
            meal, product = sublist
            dict_shopping_cart = dict_verif_modif(meal, product, dict_shopping_cart)
        else:
            # for value in dict_shopping_cart.values():
            #     if len(value) > 0:
            #         break
            #     else:
            #         return 'No products in the cart!'
            print(dict_shopping_cart)
            sorted_shopping_cart = sorted(dict_shopping_cart.items(), key=lambda x: (-len(x[1]), x[0]))
            result = ""
            for meal in sorted_shopping_cart:
                result += f"{meal[0]}:\n"
                sorted_product = sorted(meal[1])
                for product in sorted_product:
                    result += f" - {product}\n"
            return result


# ###########################
# Test_Code_1:
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
#     ))
# ---------------------------
# Output_1:
# Pizza:
#  - cheese
#  - flour
#  - ham
#  - mushrooms
# Dessert:
#  - milk
# Soup:
#  - carrots
# ###########################
# Test_Code_2:
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop', ))
# ---------------------------
# Output_2:
# Dessert:
#  - milk
# Pizza:
#  - ham
# Soup:
# ###########################
# Test_Code_3:
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
#     ))
# ---------------------------
# Output_3:
# No products in the cart!
# ###########################
