list_gifts = input().split(" ")
list_all_commands = []
command = str(input())

while command != "No Money":
    list_all_commands.append(command)
    for specific_command in range(len(list_all_commands)):
        command = list_all_commands[specific_command]
        command_list_position = specific_command
        string_command_details = "".join(command)
        list_command_details = string_command_details.split(" ")

        if list_command_details[0] == "OutOfStock":
            for specific_gift in range(len(list_gifts)):
                gift_list_position = specific_gift
                if list_gifts[gift_list_position] == list_command_details[1]:
                    list_gifts[gift_list_position] = "None"
        elif list_command_details[0] == "Required":
            if int(list_command_details[2]) <= len(list_gifts) - 1:
                list_gifts[int(list_command_details[2])] = list_command_details[1]
            else:
                continue
        elif list_command_details[0] == "JustInCase":
            list_gifts[-1] = list_command_details[1]
    command = str(input())
else:
    for gift in list_gifts:
        if gift == "None":
            list_gifts.remove(gift)
    print(" ".join(list_gifts))