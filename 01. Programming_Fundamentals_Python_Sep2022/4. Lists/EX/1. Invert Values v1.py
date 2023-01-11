original_list_strings = input().split()
new_list_strings= []
for original_number in original_list_strings:
    new_number = 0 - int(original_number)
    new_list_strings.append(new_number)
print(new_list_strings)