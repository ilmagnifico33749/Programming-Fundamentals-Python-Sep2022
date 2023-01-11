list_gifts = ['Eggs', 'StuffedAnimal', 'Cozonac', 'Sweets', 'EasterBunny', 'Eggs', 'Clothes']
list_all_commands = ['OutOfStock Eggs', 'Required Spoon 2', 'JustInCase ChocolateEgg']
command = str(input())
while command != "No Money":
    list_all_commands.append(command)
    for specific_command in range(len(list_all_commands)):
        command = list_all_commands[specific_command]
        command_list_position = specific_command
        print(f"Command Position:{command_list_position}")
        string_command_details = "".join(command)
        print(string_command_details)
        list_command_details = string_command_details.split(" ")
        print(list_command_details)

        if list_command_details[0] == "OutOfStock":
            for specific_gift in range(len(list_gifts)):
                gift_list_position = specific_gift
                if list_gifts[gift_list_position] == list_command_details[1]:
                    list_gifts[gift_list_position] = "None"
        elif list_command_details[0] == "Required":
            list_gifts[int(list_command_details[2])] = list_command_details[1]

        elif list_command_details[0] == "JustInCase":
            list_gifts[-1] = list_command_details[1]
    command = str(input())
else:
    print(list_gifts)




