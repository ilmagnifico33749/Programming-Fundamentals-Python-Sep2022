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
    for command in sorted(original_list_commands):
        command_details = command.split("-")
        command_essence = command_details.pop(1)
        filtered_list_commands.insert((sorted(original_list_commands).index(command)), command_essence)
    print(filtered_list_commands)
