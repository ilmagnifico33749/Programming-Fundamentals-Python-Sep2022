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
while command != "3:1":
    command_details = command.split()

    if command_details[0] == "merge":
        current_word = ""
        print(command)
        #------------------------------------------#
        #Times the numbers will actually be merged - BEGINNING#
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

    elif command_details[0] == "divide":
        index = command_details[1]
        word = encrypted_message.pop(int(index))
        print(f"Current Encrypted Message after the Poping: {encrypted_message}")
        print(f"Len WORD: {len([x for x in word])}")
        divider = math.floor(int(command_details[2]))
        times_to_divide = int((int(len(word))) / int(divider))
        remainder = len(word) % divider
        if remainder == 0:
            word_list = [x for x in word]
            new_letter = []
            for letter in range(len(word_list)):
                if len(word_list) > 0:
                    print(f"Index Letter: {letter}")
                    current_letter = ""
                    list_current_letters = []
                    for dividings in range(times_to_divide):
                        print(f"Diving: {dividings}")
                        current_letter = word_list.pop(0)
                        list_current_letters.append(current_letter)
                        print(f"Current Letter: {current_letter}")
                    print(f"List Current Letters: {''.join(list_current_letters)}")
                    new_letter.append(''.join(list_current_letters))
            print(new_letter)
            print(' '.join(new_letter))
            encrypted_message.insert(int(index), ' '.join(new_letter))
            print(f"New Enryptedly Decrypted Message: {encrypted_message}")

        elif remainder > 0:
            word_list = [x for x in word]
            new_letter = []
            first_part_len = int(times_to_divide * (math.floor(int(len(word_list)) / times_to_divide)) - times_to_divide)
            print(f"First Part Len: {first_part_len}")
            print("---------------------")
            print(f"FIRST PART")
            while len(word_list) > (times_to_divide + remainder):
                print(f"Div/Rem = {times_to_divide + remainder}")
                count_letters = times_to_divide
                for letter in range(len(word_list)):
                    if count_letters <= first_part_len:
                        print(f"Count Letters: {count_letters}")
                        print(f"Index Letter: {letter}")
                        current_letter = ""
                        list_current_letters = []
                        for dividings in range(times_to_divide):
                            count_letters += 1
                            print(f"Diving: {dividings}")
                            current_letter = word_list.pop(0)
                            list_current_letters.append(current_letter)
                            print(f"Current Letter: {current_letter}")
                        print(f"List Current Letters: {''.join(list_current_letters)}")
                        new_letter.append(''.join(list_current_letters))
                print(f"FIRST PART END")
                print(new_letter)
                print(' '.join(new_letter))
                print("---------------------")
                print(f"Len Word List End Part 1: {len(word_list)}")
            else:
                print("---------------------")
                print(f"SECOND PART Start")
                list_current_letters = []
                current_letter = "".join(word_list)
                list_current_letters.append(current_letter)
                print(f"Current Letter: {current_letter}")
                print(f"List Current Letters: {''.join(list_current_letters)}")
                new_letter.append(''.join(list_current_letters))
                print(new_letter)
                print(f"New Word After Being Divided: {' '.join(new_letter)}")
                print(f"SECOND PART End")
                print("---------------------")
            f"Index: {index}"
            encrypted_message.insert(int(index), ' '.join(new_letter))
            print(f"FINAL DECRYPTED MESSAGE: {encrypted_message}")

    command = input()

else:
    print(f"FINAL DECRYPTED MESSAGE: {' '.join(encrypted_message)}")
