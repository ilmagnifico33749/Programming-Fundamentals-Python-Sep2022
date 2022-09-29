command = input()
while command != "End":
    if command != "SoftUni":
        new_command = ""
        for i in range(len(command)):
            symbol = command[i]
            double_symbol = symbol * 2
            new_command += double_symbol
        print(new_command)
        command = input()
    else:
        command = input()





