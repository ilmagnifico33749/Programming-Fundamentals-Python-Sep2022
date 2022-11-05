user_input = int(input())
list_wagons = [0 for x in range(1, user_input + 1)]
print(list_wagons)

command = str(input())
while command != "End":
    command_details = command.split(" ")
    index_value = 0
    if command_details[0] == "add":
        print(f"{list_wagons[user_input-1]}")
        index_value = list_wagons[len(list_wagons) - 1]
        list_wagons.remove(list_wagons[len(list_wagons) - 1])
        list_wagons.insert((user_input - 1), (index_value + int(command_details[1])))
        print(list_wagons)
        print(f"Len: {len(list_wagons)}")
else:
    print(list_wagons)