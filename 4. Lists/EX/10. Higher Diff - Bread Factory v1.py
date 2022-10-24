#rest-2|order-10|eggs-100|rest-10

initial_energy = 100
current_energy = initial_energy
potential_new_energy = initial_energy
rest_needed = 0
initial_coins = 100
current_budget = initial_coins
potential_new_budget = initial_coins
list_events = input().split("|")
bakery_rush = True

for event in list_events:
    event_details = event.split("-")
    event_name = event_details[0]
    event_value = event_details[1]

    if event_name == "rest":
        potential_new_energy = current_energy + int(event_value)
        rest_needed = initial_energy - current_energy
        if potential_new_energy <= 100:
            current_energy = potential_new_energy
            print(f"You gained {event_value} energy.\nCurrent energy: {current_energy}.")
        else:
            current_energy = initial_energy
            print(f"You gained {rest_needed} energy.\nCurrent energy: {current_energy}.")
    elif event_name == "order":
        potential_new_energy = current_energy - 30
        if potential_new_energy >= 0:
            current_budget += int(event_value)
            print(f"You earned {event_value} coins.")
            current_energy = potential_new_energy
        else:
            current_energy += 50
            print(f"You had to rest!")
    else:
        potential_new_budget = current_budget - int(event_value)
        if potential_new_budget >= 0:
            current_budget -= int(event_value)
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            bakery_rush = False
            break

if bakery_rush == True:
    print(f"Day completed!\nCoins: {current_budget}\nEnergy: {current_energy}")





