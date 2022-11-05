# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End

user_input = input()
original_list_commands = []

def sorting_and_poping(list):
    sorted_list = sorted(list)
    new_final_list = []
    for command in range(len(sorted_list)):
        command_details = sorted_list[command].split("-")
        command_essence = command_details.pop(1)
        print(f"Command Essence: {command_essence}")
        sorted_list.remove(sorted_list[command])
        sorted_list.insert(command, command_essence)
    return sorted_list

while user_input != "End":
    original_list_commands.append(user_input)
    user_input = input()
else:
    print(sorting_and_poping(original_list_commands))