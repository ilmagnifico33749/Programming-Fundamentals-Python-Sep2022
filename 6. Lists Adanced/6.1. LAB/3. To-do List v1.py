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
    user_input = input()
else:
    sorted_list_commands = sorted(original_list_commands)
    for command in range(len(sorted_list_commands)):
        command_details = sorted_list_commands[command].split("-")
        command_essence = command_details.pop(1)
        filtered_list_commands.insert(command, command_essence)
    print(filtered_list_commands)

