weapon_name = input().split("|")

command = input()
while command != "Done":
    command_details = command.split(" ")
    action = command_details[0]

    if action == "Add":
        particle = command_details[1]
        index = int(command_details[2])
        if 0 <= abs(index) <= (len(weapon_name) - 1):
            weapon_name.insert(index, particle)

    elif action == "Remove":
        index = int(command_details[1])
        if 0 <= abs(index) <= (len(weapon_name) - 1):
            a = weapon_name.pop(index)

    elif action == "Check":
        to_check = command_details[1]
        if to_check == "Even":
            even = [weapon_name[x] for x in range(len(weapon_name)) if x % 2 == 0]
            print(" ".join(even))
        elif to_check == "Odd":
            odd = [weapon_name[x] for x in range(len(weapon_name)) if x % 2 != 0]
            print(" ".join(odd))

    command = input()

else:
    print(f"You crafted {''.join(weapon_name)}!")
