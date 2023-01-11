my_dict_order = {}

while True:
    command = input()
    while command != "buy":
        order_details = command.split(" ")
        product_name = str(order_details[0])
        product_price = float(order_details[1])
        product_quantity = int(order_details[2])

        if product_name not in my_dict_order.keys():
            my_dict_order[product_name] = {"price": product_price, "quantity": product_quantity}
        else:
            my_dict_order[product_name]["price"] = f"{product_price:.2f}"
            my_dict_order[product_name]["quantity"] += product_quantity

        command = input()

    else:
        for product in my_dict_order.keys():
            print(f'{product} -> {(float(my_dict_order[product]["price"]) * int(my_dict_order[product]["quantity"])):.2f}')

# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy
#-------------------#
# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy
#-------------------#
# CesarSalad 10.20 25
# SuperEnergy 0.80 400
# Beer 1.35 350
# IceCream 1.50 25
# buy
#-------------------#
