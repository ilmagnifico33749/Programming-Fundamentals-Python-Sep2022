# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End

original_list_commands = 10 * [0]

while True:
    user_input = input()
    if user_input == "End":
        break
    else:
        command_details = user_input.split("-")
        command_importance = int(command_details[0]) - 1
        command_essence = command_details[1]
        original_list_commands.pop(command_importance)
        original_list_commands.insert(command_importance, command_essence)
final_list_commands = [command for command in original_list_commands if command != 0]
print(final_list_commands)

