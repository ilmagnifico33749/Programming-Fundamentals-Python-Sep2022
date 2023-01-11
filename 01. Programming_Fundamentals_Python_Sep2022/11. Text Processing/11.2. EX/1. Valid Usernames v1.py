command = "Jeff, john45, ab, cd, peter-ivanov, @smith"
command_details = command.split(", ")

for username in command_details:
    validity = False
    if 3 <= len(username) <= 16:
        validity = True
        for symbol in username:
            if symbol.isalnum() is True or symbol == "-" or symbol == "_":
                validity = True
            else:
                validity = False
                break
    if validity is True:
        print(username)
