list_characters = input().split(", ")
my_dictionary = {symbol: ord(symbol) for symbol in list_characters}
print(my_dictionary)