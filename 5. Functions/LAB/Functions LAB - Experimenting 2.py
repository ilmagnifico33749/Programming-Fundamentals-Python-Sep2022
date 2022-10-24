#def function_name(parameter: type):
#    statement(s)

list_numbers_original = input().split(" ")
list_numbers_abs_value = []

for num in list_numbers_original:
    list_numbers_abs_value.append(abs(float(num)))
print(list_numbers_abs_value)

