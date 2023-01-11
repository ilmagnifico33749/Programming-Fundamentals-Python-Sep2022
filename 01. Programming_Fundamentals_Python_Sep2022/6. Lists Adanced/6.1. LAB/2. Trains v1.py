user_input = int(input())
list_wagons = [0 for x in range(1, user_input + 1)]

command = str(input())
while command != "End":
    command_details = command.split(" ")
    if command_details[0] == "add":
        list_wagons[user_input - 1] += int(command_details[1])
    elif command_details[0] == "insert":
        list_wagons[int(command_details[1])] += int(command_details[2])
    elif command_details[0] == "leave":
        list_wagons[int(command_details[1])] -= int(command_details[2])
    command = str(input())
else:
    print(list_wagons)