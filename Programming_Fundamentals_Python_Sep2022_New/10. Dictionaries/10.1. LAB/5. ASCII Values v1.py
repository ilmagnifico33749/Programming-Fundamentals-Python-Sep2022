list_characters = input().split(", ")
my_dict1 = {}
for symbol in list_characters:
    my_dict1[str(symbol)] = ord(str(symbol))
print(my_dict1)