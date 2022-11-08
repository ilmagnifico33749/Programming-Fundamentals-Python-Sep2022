number_wagons = int(input())
list_wagons = [0 * number_wagons for x in range(number_wagons)]
command = input()

while command != "End":
    command_details = command.split(" ")
    if command_details[0] == "add":
        current_wagon = list_wagons.pop((len(list_wagons) - 1))
        new_value_current_wagon = int(current_wagon) + int(command_details[1])
        list_wagons.insert((len(list_wagons) + 1), new_value_current_wagon)
    elif command_details[0] == "insert":
        current_wagon = list_wagons.pop(int(command_details[1]))
        new_value_current_wagon = int(current_wagon) + int(command_details[2])
        list_wagons.insert(int(command_details[1]), int(new_value_current_wagon))
    elif command_details[0] == "leave":
        current_wagon = list_wagons.pop(int(command_details[1]))
        new_value_current_wagon = int(current_wagon) - int(command_details[2])
        list_wagons.insert(int(command_details[1]), new_value_current_wagon)
    command = input()
else:
    print(list_wagons)