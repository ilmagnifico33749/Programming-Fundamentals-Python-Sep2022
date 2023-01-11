# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End

user_input = input()
original_list_commands = []
filtered_list_commands = []
while user_input != "End":
    original_list_commands.append(user_input)
    sorted_list = sorted(original_list_commands)
    user_input = input()
else:
    for command in range(len(sorted_list)):
        command_details = sorted_list[command].split("-")
        command_essence = command_details.pop(1)
        sorted_list.remove(sorted_list[command])
        sorted_list.insert(command, command_essence)
    print(sorted_list)