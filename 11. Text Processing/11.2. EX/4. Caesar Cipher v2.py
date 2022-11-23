
def encrypting(original_message):
    new_message = ""
    for symbol in original_message:
        new_message += chr((ord(symbol)) + 3)
    return new_message

    # OR

    # new_message = []
    # for symbol in original_message:
    #     new_message.append(chr((ord(symbol)) + 3))
    # return "".join(new_message)

print(encrypting(input()))

#----------------------------------#
# input_1: Programming is cool!
# output_1: Surjudpplqj#lv#frro$
#----------------------------------#
# input_2: One year has 365 days.
# output_2: Rqh#|hdu#kdv#698#gd|v1
#----------------------------------#