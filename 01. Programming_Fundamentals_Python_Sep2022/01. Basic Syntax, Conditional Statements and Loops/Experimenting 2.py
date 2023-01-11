# a = input()
# print(ord(a))
# print(chr(97))
# new_command = ""

initial_quantity_decorations = int(input())
all_days = int(input())
days_passed = 0
total_cost = 0
points_spirit = 0
decoration_cost = 0
points_spirit_gained_daily = 0
daily_expenses = 0
price_ornament_set = 2
points_ornament_set = 5
price_tree_skirt = 5
points_tree_skirt = 3
price_tree_garland = 3
points_tree_garland = 10
price_tree_lights = 15
points_tree_lights = 17

for days_passed in range(1, all_days + 1):
    if days_passed % 11 != 0:
        quantity_decorations = initial_quantity_decorations
    else:
        quantity_decorations = initial_quantity_decorations + 2

    if days_passed % 2 == 0:
        daily_expenses = price_ornament_set * quantity_decorations
        total_cost += daily_expenses
        points_spirit_gained_daily = points_ornament_set
        points_spirit += points_spirit_gained_daily
        print(f"Day {days_passed}")
        print(total_cost)
        print(points_spirit)

    if days_passed % 3 == 0:
        daily_expenses = (price_tree_skirt + price_tree_garland) * quantity_decorations
        total_cost += daily_expenses
        points_spirit_gained_daily = (points_tree_skirt + points_tree_garland)
        points_spirit += points_spirit_gained_daily
        print(f"Day {days_passed}")
        print(total_cost)
        print(points_spirit)

    if days_passed % 5 == 0:
        daily_expenses = price_tree_lights * quantity_decorations
        total_cost += daily_expenses
        points_spirit_gained_daily = points_tree_lights
        points_spirit += points_spirit_gained_daily
        if days_passed % 3 == 0:
            points_spirit += 30
        print(f"Day {days_passed}")
        print(total_cost)
        print(points_spirit)

    if days_passed % 10 == 0:
        points_spirit_gained_daily = -20
        points_spirit += points_spirit_gained_daily
        daily_expenses += (price_tree_skirt + price_tree_garland + price_tree_lights)
        total_cost += daily_expenses
        print(f"Day {days_passed}")
        print(total_cost)
        print(points_spirit)

if all_days % 10 == 0:
    points_spirit_gained_daily = -30
    points_spirit += points_spirit_gained_daily
    print(f"Day {days_passed}")
    print(total_cost)
    print(points_spirit)


print(f"Total Cost: {total_cost}\nTotal Spirit: {points_spirit}")

