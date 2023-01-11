def user_input_list(user_input):
    list_user_input = []
    while user_input != "End":
        list_user_input.append(user_input)
        user_input = input()
    else:
        return list_user_input

def list_manipulation_one(list):
    new_list = []
    list_tasks = ["0" * 1 for x in range(10)]
    for command in sorted(list):
        command_details = command.split("-")
        command_essence = command_details.pop(1)
        new_list.insert(len(new_list), command_essence)
        a = list_tasks.pop(int(command_details[0]))
        list_tasks.insert(int(command_details[0]), command_essence)
    return [x for x in list_tasks if x != "0"]

print(list_manipulation_one(user_input_list(input())))