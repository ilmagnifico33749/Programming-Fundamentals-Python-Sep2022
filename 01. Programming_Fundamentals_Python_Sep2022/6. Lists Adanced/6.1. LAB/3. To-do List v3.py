# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End

user_input = input()
original_list_commands = []
filtered_list_commands = []


def sorting_and_poping(list):
    sorted_list = sorted(list)
    new_final_list = []
    for command in sorted_list:
        command_details = command.split("-")
        command_essence = command_details.pop(1)
        new_final_list.append(command_essence)
    return new_final_list

while user_input != "End":
    original_list_commands.append(user_input)
    user_input = input()
else:
    print(sorting_and_poping(original_list_commands))




