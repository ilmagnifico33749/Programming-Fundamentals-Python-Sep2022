encrypted_message = input()
command = input()

while command != "Reveal":
    command_details = command.split(":|:")
    instruction = command_details[0]

    if instruction == "InsertSpace":
        list_encrypted_message = list(encrypted_message)
        list_encrypted_message.insert(int(command_details[1]), " ")
        encrypted_message = ''.join(list_encrypted_message)
        print(encrypted_message)
    elif instruction == "Reverse":
        substring = command_details[1]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, "", 1)
            encrypted_message = encrypted_message + (''.join(reversed(substring)))
            print(encrypted_message)
        else:
            print(f"error")
    elif instruction == "ChangeAll":
        current_strings = command_details[1]
        new_strings = command_details[2]
        encrypted_message = encrypted_message.replace(current_strings, new_strings)
        print(encrypted_message)

    command = input()
else:
    print(f"You have a new text message: {encrypted_message}")

# ----------------------------------------------#
# ----------------------------------------------#
# Input_1:
# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal
# ----------------------------------------------#
# Output_1:
# hellodar!gnil
# hellodarling!
# hello darling!
# You have a new text message: hello darling!
# ----------------------------------------------#
# ----------------------------------------------#
# Input_2:
# Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal
# ----------------------------------------------#
# Output_2:
# Howare?uoy
# Howareyou?
# error
# How areyou?
# How are you?
# You have a new text message: How are you?
# ----------------------------------------------#
# ----------------------------------------------#

