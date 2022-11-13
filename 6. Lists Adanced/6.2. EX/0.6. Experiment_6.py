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

command = input()
while command != "3:1":
    command_details = command.split()
#-------------------------------------------------------------------#
    if command_details[0] == "merge":
        #words_to_merge = [encrypted_message[word] for word in range(len(encrypted_message)) if word
        #                 in range(int(command_details[1]), int(command_details[2]) + 1)]
        words_to_merge = [encrypted_message.pop(int(command_details[1])) for times in range((int(command_details[2]) + 1) - int(command_details[1]))]
        print(words_to_merge)
        print(encrypted_message)
        encrypted_message.insert(int(command_details[1]), ''.join(words_to_merge))
        print(f"Merging Completed: {encrypted_message}")
#-------------------------------------------------------------------#

    elif command_details[0] == "divide":
        word_to_divide = str(''.join([encrypted_message.pop(word) for word in range(len(encrypted_message)) if word == int(command_details[1])]))
        print(word_to_divide)
        #letters_words = [word_to_divide[letters] for letters in range(len(word_to_divide))]
        #print(letters_words)
        letters_word = [letter for letter in word_to_divide]
        print(letters_word)


    break

