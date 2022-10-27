symbol_1 = ord(input())
symbol_2 = ord(input())
list_filtered_symbols= []

def filtering_function(symbol):
    list_filtered_symbols.append(chr(symbol))

def listing_function(num_1, num_2):
    for sym in range(int(num_1) + 1, int(num_2)):
        filtering_function(sym)
    return " ".join(list_filtered_symbols)

print(listing_function(symbol_1, symbol_2))