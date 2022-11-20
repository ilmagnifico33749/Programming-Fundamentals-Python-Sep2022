my_dict_force_users = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        command_details = command.split(" | ")
        force_side, person = command_details
        person_already_present = False
        for value in my_dict_force_users.values():
            if person in value:
                person_already_present = True
                break
        else:
            if force_side not in my_dict_force_users.keys():
                my_dict_force_users[force_side] = [person]
            else:
                my_dict_force_users[force_side].append()
    elif "->" in command:
        command_details = command.split(" -> ")
        person, force_side = command_details
        for key, value in my_dict_force_users.items():
            if person in value:
                my_dict_force_users[key].pop(value.index(person))
                break
        my_dict_force_users[force_side].append(person)
        print(f"{person} joins the {force_side} side!")
    command = input()
else:
    for key in my_dict_force_users.keys():
        if len(my_dict_force_users[key]) > 0:
            print(f"Side: {key}, Members: {len(my_dict_force_users[key])} ")
            for jedi in my_dict_force_users[key]:
                print(f"! {jedi}")

# --------------------------#
# Light | Peter
# Dark | Kim
# Light | Kim
# Lumpawaroo
# --------------------------#
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo
# --------------------------#
