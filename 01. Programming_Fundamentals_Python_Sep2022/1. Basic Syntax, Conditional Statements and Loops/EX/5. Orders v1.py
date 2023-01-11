number_of_orders = int(input())
order_total_value = 0.00
for o in range(0, number_of_orders, 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_need_per_day = int(input())
    order_value = price_per_capsule * days * capsules_need_per_day
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_need_per_day <= 2000:
        order_total_value += float(order_value)
        print(f"The price for the coffee is: ${order_value:.2f}")
    else:
        pass
print(f"Total: ${order_total_value:.2f}")

