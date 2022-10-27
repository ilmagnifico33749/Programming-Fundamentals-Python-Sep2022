symbol_1 = int(input())
symbol_2 = int(input())

list_filtered_symbols = []
for symbol in range((symbol_1), symbol_2):
    print(int(symbol))
    print(f"Symbol {symbol}")
    list_filtered_symbols.append(chr(symbol))
