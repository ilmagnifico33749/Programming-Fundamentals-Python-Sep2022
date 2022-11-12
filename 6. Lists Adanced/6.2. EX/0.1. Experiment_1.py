#===============================================#
# Input_1:                                      #
# - Ivo Johny Tony Bony Mony                    #
# - merge 0 3                                   #
# - merge 3 4                                   #
# - merge 0 3                                   #
# - 3:1                                         #
# Output: IvoJohnyTonyBonyMony                  #
#-----------------------------------------------#
# Input_2:                                      #
# - abcd efgh ijkl mnop qrst uvwx yz            #
# - merge 4 10                                  #
# - divide 4 5                                  #
# - 3:1                                         #
#Output_2: abcd efgh ijkl mnop qr st uv wx yz   #
#===============================================#

import math

encrypted_message = input().split(" ")
print(encrypted_message)
print(len(encrypted_message))

command = input()
command_details = command.split()

if command_details[0] == "merge":
    current_word = ""
    print(command)
    # ------------------------------------------#
    # Times the numbers will actually be merged - BEGINNING#
    actual_number_words_to_be_merged = 0
    requested_number_words_to_merge = int(command_details[2]) - int(command_details[1]) + 1
    print(f"Requested Number of words to merge: {requested_number_words_to_merge}")
    possible_number_words_to_merge = len(encrypted_message) - (int(command_details[1]))
    print(f"Possible number of words to merge: {possible_number_words_to_merge}")
    if requested_number_words_to_merge <= possible_number_words_to_merge:
        actual_number_words_to_be_merged = requested_number_words_to_merge
    else:
        actual_number_words_to_be_merged = possible_number_words_to_merge
    print(f"Actual Number of Words to Be Merged: {actual_number_words_to_be_merged}")
    # Times the numbers will actually be merged - BEGINNING#
    # ------------------------------------------#
    current_word = str()
    list_words_to_merge = []
    for words in range(len(encrypted_message)):
        for times in range(actual_number_words_to_be_merged):
            if words == int(command_details[1]):
                current_word = encrypted_message.pop(int(command_details[1]))
                print(f"Current Word: {current_word}")
                list_words_to_merge.append(current_word)
    print(list_words_to_merge)
    print(encrypted_message)
    print("Modif Mess")
    encrypted_message.insert(int(command_details[1]), ''.join(list_words_to_merge))
    print("Mess Modified")
    print(f"Message: {encrypted_message}")

print(f"FINAL DECRYPTED MESSAGE: {' '.join(encrypted_message)}")
