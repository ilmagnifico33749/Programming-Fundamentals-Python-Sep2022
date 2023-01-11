original_message = input()
new_message = ""

for symbol in original_message:
    new_symbol = chr((ord(symbol)) + 3 )
    new_message += new_symbol

# OR

# new_message = []
# for symbol in original_message:
#     new_symbol = chr((ord(symbol)) + 3)
#     new_message.append(new_symbol)
# return "".join(new_message)

print(new_message)

#----------------------------------#
# input_1: Programming is cool!
# output_1: Surjudpplqj#lv#frro$
#----------------------------------#
# input_2: One year has 365 days.
# output_2: Rqh#|hdu#kdv#698#gd|v1
#----------------------------------#