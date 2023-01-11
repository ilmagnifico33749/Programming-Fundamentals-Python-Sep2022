#1 2.5 -3 -4.5
#-0 1 10 -6.66

list_orig_numbers = input().split(" ")
list_abs_val_num = []

def function_abs_value(number):
    abs_value_number = abs(number)
    list_abs_val_num.append(abs_value_number)

for i in list_orig_numbers:
    function_abs_value(float(i))

print(list_abs_val_num)

