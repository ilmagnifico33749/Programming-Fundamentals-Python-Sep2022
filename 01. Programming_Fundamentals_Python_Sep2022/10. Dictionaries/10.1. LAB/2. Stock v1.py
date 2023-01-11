stock = {}
list_stock = input().split(" ")
for product in range(0, len(list_stock), 2):
    stock[list_stock[product]] = list_stock[product + 1]
list_availability_check = input().split(" ")
for desired_product in list_availability_check:
    if desired_product in stock:
        print(f"We have {stock[desired_product]} of {desired_product} left")
    else:
        print(f"Sorry, we don't have {desired_product}")