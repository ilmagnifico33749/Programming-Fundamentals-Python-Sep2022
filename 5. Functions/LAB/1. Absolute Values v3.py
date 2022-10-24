#1 2.5 -3 -4.5
#-0 1 10 -6.66
list_orig_numbers = input().split(" ")

def function_abs_value(number):
    list_abs_val_num = []
    for num in list_orig_numbers:
        abs_value_number = abs(float(num))
        list_abs_val_num.append(abs_value_number)
    return list_abs_val_num

print(function_abs_value(list_orig_numbers))