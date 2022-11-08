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
        command_essence = "".join(command_details[1:])
        new_list.append(command_essence)
    return new_list

print(list_manipulation_one(user_input_list(input())))