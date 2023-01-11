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

    if command_details[0] == "merge":
        word_to_merge = [encrypted_message[word] for word in range(len(encrypted_message)) if word
                         in range(int(command_details[1]), int(command_details[2]))]

    elif command_details[0] == "divide":
        index = command_details[1]
        word = encrypted_message.pop(int(index))
        divider = math.floor(int(command_details[2]))
        times_to_divide = int((int(len(word))) / int(divider))
        remainder = len(word) % divider
        if remainder == 0:
            word_list = [x for x in word]
            new_letter = []
            for letter in range(len(word_list)):
                if len(word_list) > 0:
                    current_letter = ""
                    list_current_letters = []
                    for dividings in range(times_to_divide):
                        current_letter = word_list.pop(0)
                        list_current_letters.append(current_letter)
                    new_letter.append(''.join(list_current_letters))
            encrypted_message.insert(int(index), ' '.join(new_letter))

        elif remainder > 0:
            word_list = [x for x in word]
            new_letter = []
            first_part_len = int(times_to_divide * (math.floor(int(len(word_list)) / times_to_divide)) - times_to_divide)
            while len(word_list) > (times_to_divide + remainder):
                count_letters = times_to_divide
                for letter in range(len(word_list)):
                    if count_letters <= first_part_len:
                        current_letter = ""
                        list_current_letters = []
                        for dividings in range(times_to_divide):
                            count_letters += 1
                            current_letter = word_list.pop(0)
                            list_current_letters.append(current_letter)
                        new_letter.append(''.join(list_current_letters))
            else:
                list_current_letters = []
                current_letter = "".join(word_list)
                list_current_letters.append(current_letter)
                new_letter.append(''.join(list_current_letters))
            encrypted_message.insert(int(index), ' '.join(new_letter))

    command = input()

else:
    print(f"{' '.join(encrypted_message)}")
