#command = int(input())

#for whole_num in range(1, command + 1):
#    whole_num_string = str(whole_num)
#    sum_digits_number = 0
#    for indiv_int_num in range(len(whole_num_string)):
#        symbol = int(whole_num_string[indiv_int_num])
#        sum_digits_number += symbol
#        if sum_digits_number == 5 or sum_digits_number == 7 or sum_digits_number == 11:
#            special_number = True
#        else:
#            special_number = False
#    print(f"{whole_num} -> {special_number}")


for i in range(len(word_one)):
    left_part = word_two[:i +1]
    right_part = word_one[i + 1:]

import sys
eternity = +sys.maxsize

initial_year = int(input())
for year in range(initial_year, 1024, 1):
    current_year = int(year)
    string_current_year = str(year)
    for numbers in range(len(string_current_year)):
        left_part = string_current_year[:numbers + 1]
        right_part = string_current_year[numbers + 1:]
        specific_number = string_current_year[numbers]
        if specific_number in range(len(left_part)):
            continue
        else:
            print(current_year)
            break

