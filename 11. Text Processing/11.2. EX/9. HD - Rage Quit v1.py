user_input = input()

current_part = ""
times_to_print = 0
final_message = ""

for symbol in range(len(user_input)):
    current_symbol = user_input[symbol]
    if current_symbol.isnumeric() == False:
        current_part += current_symbol
    else:
        times_to_print = int(current_symbol)
        final_message += (str(current_part).upper() * times_to_print)
        current_part = ""

print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)

# ---------------------------#
# input_1: a3
# output_1:
# Unique symbols used: 1
# AAA
# ---------------------------#
# input_1: aSd2&5s@1
# output_2:
# Unique symbols used: 5
# ASDASD&&&&&S@
# ---------------------------#
