import sys
highest_number = -sys.maxsize
number_of_inputs = 3
for i in range(number_of_inputs):
    a = int(input())
    if a > highest_number:
        highest_number = a
print(highest_number)