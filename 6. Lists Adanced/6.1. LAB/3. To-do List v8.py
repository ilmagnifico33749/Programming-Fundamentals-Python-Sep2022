def user_input_list(user_input):
    list_user_input = []
    while user_input != "End":
        list_user_input.append(user_input)
        user_input = input()
    else:
        return list_user_input

def list_manipulation_one(list):
    new_list = []
    for command in sorted(list):
        command_details = command.split("-")
        command_essence = command_details.pop(1)
        new_list.insert(len(new_list), command_essence)
    return new_list

print(list_manipulation_one(user_input_list(input())))