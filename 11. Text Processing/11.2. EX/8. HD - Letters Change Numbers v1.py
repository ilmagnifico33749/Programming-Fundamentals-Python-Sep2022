# 80 /10 points from Judge ... however the output is fine.

user_input = input()
list_all_commands = user_input.split(" ")
final_sum = 0.00

for command in range(len(list_all_commands)):
    if len(list_all_commands[command]) >= 3:

        current_result = 0.00
        list_current_command = [x for x in list_all_commands[command]]
        first_letter = list_current_command.pop(0)
        last_letter = list_current_command.pop((len(list_current_command)-1))
        current_number = int("".join(list_current_command))

        if first_letter.islower() == True:
            current_result = current_number * (ord(first_letter) - 96)
        elif first_letter.isupper() == True:
            current_result = current_number / (ord(first_letter) - 64)

        if last_letter.islower() == True:
            current_result = current_result + (ord(last_letter) - 96)
            final_sum += current_result
        elif last_letter.isupper() == True:
            current_result = current_result - (ord(last_letter) - 64)
            final_sum += current_result

print(f"{final_sum:.2f}")


# a1A
# A12b s17G
# P34562Z q2576f   H456z
