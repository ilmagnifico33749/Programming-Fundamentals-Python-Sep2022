stock = {}
command = input()

while command != "statistics":
    command_details = command.split(": ")
    key_product = command_details[0]
    value_quantity = command_details[1]
    if key_product not in stock:
        stock[key_product] = int(value_quantity)
    else:
        stock[key_product] += int(value_quantity)
    command = input()
else:
    print(f"Products in stock: ")
    for (key_product, value_quantity) in stock.items():
        print(f"- {key_product}: {value_quantity}")
    print(f"Total Products: {len(stock.keys())}\nTotal Quantity: {sum(stock.values())}")

# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics
#
# eggs: 10
# bread: 6
# cheese: 8
# milk: 7
# statistics
