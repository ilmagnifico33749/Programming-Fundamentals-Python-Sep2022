original_budget = int(input())
current_budget = original_budget
command = input()
while command != "End":
    product_price = int(command)
    current_budget -= product_price
    while current_budget > 0 and command != "End":
        continue
    else:
        print(f"You went in overdraft!")
        break
    command = input()
else:
    print(f"You bought everything needed.")
