user_input = int(input())
list_wagons = [0 for x in range(1, user_input + 1)]

command = str(input())
while command != "End":
    command_details = command.split(" ")
    index_value = 0
    if command_details[0] == "add":
        index_value = list_wagons[len(list_wagons) - 1]
        list_wagons.remove(list_wagons[len(list_wagons) - 1])
        list_wagons.insert((user_input - 1), (index_value + int(command_details[1])))
    elif command_details[0] == "insert":
        index_value = list_wagons.pop(int(command_details[1]))
        list_wagons.insert(int(command_details[1]), (index_value + int(command_details[2])))
    elif command_details[0] == "leave":
        index_value = list_wagons.pop(int(command_details[1]))
        list_wagons.insert(int(command_details[1]), (index_value - int(command_details[2])))
    command = str(input())
else:
    print(list_wagons)
