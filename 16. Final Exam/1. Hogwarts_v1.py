spell_ciphered = input()

list_valid_commands = ["Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]
list_actions = []

actions = input()
while actions != "Abracadabra":
    action_details = actions.split(" ")
    instruction = action_details[0]
    if instruction in list_valid_commands:
        list_actions.append(actions)
    else:
        print("The spell did not work!")
    actions = input()

for command in list_actions:
    command_details = command.split(" ")
    action_to_take = command_details[0]

    if action_to_take == "Abjuration":
        spell_ciphered = spell_ciphered.upper()
        print(spell_ciphered)

    elif action_to_take == "Necromancy":
        spell_ciphered = spell_ciphered.lower()
        print(spell_ciphered)

    elif action_to_take == "Illusion":
        index = command_details[1]
        letter = command_details[2]
        if index.isnumeric() == True:
            if 0 <= int(index) < (len(spell_ciphered)):
                spell_ciphered = spell_ciphered.replace(spell_ciphered[int(index)], letter)
                print(f"Done!")
            else:
                print(f"The spell was too weak.")
        else:
            print(f"The spell was too weak.")

    elif action_to_take == "Divination":
        first_substring = command_details[1]
        second_substring = command_details[2]
        if first_substring in spell_ciphered:
            spell_ciphered = spell_ciphered.replace(first_substring, second_substring)
            print(spell_ciphered)
        else:
            pass

    elif action_to_take == "Alteration":
        substring = command_details[1]
        if substring in spell_ciphered:
            spell_ciphered = spell_ciphered.replace(substring, "")
            print(spell_ciphered)
        else:
            pass


# A7ci0
# Illusion 1 c
# Illusion 4 o
# Abjuration
# Abracadabra

# SwordMaster
# Target Target Target
# Abjuration
# Necromancy
# Alteration master
# Abracadabra