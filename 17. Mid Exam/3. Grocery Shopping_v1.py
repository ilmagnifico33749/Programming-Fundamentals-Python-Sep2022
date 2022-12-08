list_products = input().split("|")

command = input()
while command != "Shop!":
    command_details = command.split("%")
    action = command_details[0]

    if action == "Important":
        product = command_details[1]
        if product in list_products:
            list_products.remove(product)

        list_products.insert(0, product)

    elif action == "Add":
        product = command_details[1]
        if product not in list_products:
            list_products.append(product)
        else:
            print(f"The product is already in the list.")

    elif action == "Swap":
        product_one = command_details[1]
        product_two = command_details[2]
        missing_product = ""
        if product_one in list_products and product_two in list_products:
            index_product_one = list_products.index(product_one)
            index_product_two = list_products.index(product_two)
            list_products[index_product_one], list_products[index_product_two] = list_products[index_product_two], list_products[index_product_one]
        else:
            if product_one not in list_products:
                missing_product = product_one
            elif product_two not in list_products:
                missing_product = product_two
            print(f"Product {missing_product} missing!")

    elif action == "Remove":
        product = command_details[1]
        if product in list_products:
            list_products.remove(product)
        else:
            print(f"Product {product} isn't in the list.")

    elif action == "Reversed":
        list_products.reverse()

    command = input()

else:
    for product in range(len(list_products)):
        print(f"{int(product) + 1}. {list_products[product]}")
