my_dict = {'Count_disliked_meals': 0}

command = input()

while command != "Stop":
    command_details = command.split("-")
    reaction = command_details[0]
    guest_name = command_details[1]
    meal = command_details[2]

    if reaction == "Like":
        if guest_name not in my_dict.keys():
            my_dict[guest_name] = {meal: reaction}
        else:
            if meal in my_dict[guest_name].keys():
                pass
            elif meal not in my_dict[guest_name].keys():
                my_dict[guest_name][meal] = reaction

    elif reaction == "Dislike":
        if guest_name in my_dict.keys():
            if meal in my_dict[guest_name].keys():
                del my_dict[guest_name][meal]
                print(f"{guest_name} doesn't like the {meal}.")
                my_dict['Count_disliked_meals'] += 1
            else:
                print(f"{guest_name} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest_name} is not at the party.")

    command = input()

else:
    for key, value in my_dict.items():
        if key != "Count_disliked_meals":
            print(f"{key}: {', '.join(my_dict[key].keys())}")
    print(f"Unliked meals: {my_dict['Count_disliked_meals']}")

# Like-Krisi-shrimps
# Like-Krisi-soup
# Like-Penelope-dessert
# Like-Misho-salad
# Stop

