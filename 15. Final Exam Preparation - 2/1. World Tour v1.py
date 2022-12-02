all_stops = input()
command = input()

while command != "Travel":
    command_details = command.split(":")
    instruction = command_details[0]

    if instruction == "Add Stop":
        index = int(command_details[1])
        string = command_details[2]
        first_part = all_stops[:index]
        second_part = all_stops[index:]
        all_stops = first_part + string + second_part
        print(all_stops)

    elif instruction == "Remove Stop":
        starting_index = int(command_details[1])
        ending_index = int(command_details[2]) + 1
        string_to_remove = all_stops[starting_index:ending_index]
        all_stops = all_stops.replace(string_to_remove, "")
        print(all_stops)

    elif instruction == "Switch":
        old_string = command_details[1]
        new_string = command_details[2]
        all_stops = all_stops.replace(old_string, new_string)
        print(all_stops)

    command = input()

else:
    print(f"Ready for world tour! Planned stops: {all_stops}")

# ------------------------------------------
# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel
# ------------------------------------------
# Albania:Bulgaria:Cyprus:Deuchland
# Add Stop:3:Nigeria
# Remove Stop:4:8
# Switch:Albania: Azərbaycan
# Travel
# ------------------------------------------
