input_product_name = str(input())
input_product_quantity = int(input())

def order_calculator(product, quantity):
    product_price = 0.00
    if product == "coffee":
        product_price = 1.50
    elif product == "water":
        product_price = 1.00
    elif product == "coke":
        product_price = 1.40
    elif product == "snacks":
        product_price = 2.00
    order_price = (f"{product_price * float(input_product_quantity):.2f}")
    print(order_price)

order_calculator(input_product_name, input_product_quantity)