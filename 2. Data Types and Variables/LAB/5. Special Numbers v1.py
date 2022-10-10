command = int(input())

for whole_num in range(1, command + 1):
    whole_num_string = str(whole_num)
    sum_digits_number = 0
    for indiv_int_num in range(len(whole_num_string)):
        symbol = int(whole_num_string[indiv_int_num])
        sum_digits_number += symbol
        if sum_digits_number == 5 or sum_digits_number == 7 or sum_digits_number == 11:
            special_number = True
        else:
            special_number = False
    print(f"{whole_num} -> {special_number}")