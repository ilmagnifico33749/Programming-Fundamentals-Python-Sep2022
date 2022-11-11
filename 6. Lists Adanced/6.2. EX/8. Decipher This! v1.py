#===============================#
# Input_1: 72olle 103doo 100ya  #
# Output_1: Hello good day      #
#-------------------------------#
# Input_1: 82yade 115te 103o    #
# Input_2: Ready set go         #
#===============================#
def message_decryption(encrypted_message):
    decrypted_message = []
    for word in encrypted_message:
        first_letter_encrypted = []
        rest_of_letters_encrypted = []
        list_ascii_numbers = [x for x in range(48, 57+1)]
        list_acii_letters_capital = [x for x in range(65, 90+1)] and [x for x in range(97, 122+1)]
        list_ascii_letters_low_case = [x for x in range(97, 122+1)]
        for symbol in word:
            if ord(symbol) in list_ascii_numbers:
                first_letter_encrypted.append(symbol)
            elif ord(symbol) in list_acii_letters_capital or symbol in list_ascii_letters_low_case:
                rest_of_letters_encrypted.append(symbol)
        first_letter_decrypted = chr(int("".join(first_letter_encrypted)))
        rest_of_letters_encrypted[0], rest_of_letters_encrypted[len(rest_of_letters_encrypted)-1] \
            = rest_of_letters_encrypted[len(rest_of_letters_encrypted)-1], rest_of_letters_encrypted[0]
        rest_of_letters_decrypted = "".join(rest_of_letters_encrypted)
        decrypted_word = first_letter_decrypted + rest_of_letters_decrypted
        decrypted_message.append(decrypted_word)
    return " ".join(decrypted_message)

print(message_decryption(input().split(" ")))