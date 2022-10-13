group_size = int(input())
days_adv = int(input())
budget = 0
income = 50
expenses = group_size * 2

for day in range(days_adv):
    if day % 3 == 0 and day != 5:
        expenses = group_size * 5
    if day % 5 == 0:
        income = 70
        if day % 3 == 0:
            expenses = group_size * 7
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    budget += income
    budget -= expenses

gains_per_group_member = int(budget / group_size)
print(f"{group_size} companions received {gains_per_group_member} coins each.")

