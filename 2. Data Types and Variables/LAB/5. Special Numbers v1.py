command = int(input())
special_number = True
sum_digits_number = 0
for integer in range(1, command, 1):
    integer_integer = int(integer)
    for number in range(integer_integer):
        sum_digits_number += integer_integer[number]
        print(sum())
        if sum_digits_number == 5 or sum_digits_number == 7 or sum_digits_number == 11:
            special_number == True
        else:
            special_number == False
    print(f"{number} -> {special_number}")



