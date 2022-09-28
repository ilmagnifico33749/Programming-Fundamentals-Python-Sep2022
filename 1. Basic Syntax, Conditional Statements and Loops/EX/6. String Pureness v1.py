number_strings = int(input())
pureness = True
for n in range(number_strings):
    command = str(input())
    for i in range(len(command)):
        symbol = command[i]
        if symbol == "," or symbol == "." or symbol == "_":
            pureness = False
    if pureness is True:
        print(f"{command} is pure.")
    else:
        print(f"{command} is not pure!")