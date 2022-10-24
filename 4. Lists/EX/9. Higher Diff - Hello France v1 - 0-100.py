#Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
#120

list_items_on_market = input().split("|")
initial_budget = float(input())
current_budget = initial_budget
money_spent_buying = 0.00
money_gained_selling = 0.00
selling_price_item = 0.00
list_price_item_for_sell = []

for items in list_items_on_market:
    item_details = items.split("->")
    item_name = str(item_details[0])
    item_price_buying = float(item_details[1])
    if item_name == "Clothes":
        if item_price_buying <= 50.00:
            if current_budget >= item_price_buying:
                current_budget -= item_price_buying
                selling_price_item = round((item_price_buying * 1.4), 2)
                list_price_item_for_sell.append(str(selling_price_item))
                money_gained_selling += selling_price_item
    if item_name == "Shoes":
        if item_price_buying <= 35.00:
            if current_budget >= item_price_buying:
                current_budget -= item_price_buying
                selling_price_item = round((item_price_buying * 1.4), 2)
                list_price_item_for_sell.append(str(selling_price_item))
                money_gained_selling += selling_price_item
    if item_name == "Accessories":
        if item_price_buying <= 20.50:
            if current_budget >= item_price_buying:
                current_budget -= item_price_buying
                selling_price_item = round((item_price_buying * 1.4), 2)
                list_price_item_for_sell.append(str(selling_price_item))
                money_gained_selling += selling_price_item

final_budget = current_budget + money_gained_selling
money_spent = initial_budget - current_budget
profit = money_gained_selling - money_spent

print(" ".join(list_price_item_for_sell))
print(f"Profit: {profit:.2f}")
if final_budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")