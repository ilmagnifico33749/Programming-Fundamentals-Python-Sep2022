symbol_1 = ord(input())
symbol_2 = ord(input())
print(symbol_1)
print(symbol_2)
list_filtered_symbols= []

def filtering_function(symbol):
    list_filtered_symbols.append(chr(symbol))


for sym in range(int(symbol_1) + 1, int(symbol_2)):
    filtering_function(sym)

print(" ".join(list_filtered_symbols))