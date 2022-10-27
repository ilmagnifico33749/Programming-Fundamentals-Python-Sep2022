initial_num = int(input())

def list_from_integer(integer):
    string_from_integer = str(integer)
    list_from_integer = []
    for symbol in range(len(string_from_integer)):
        print(f"Symbol: {symbol}")
        print(str(string_from_integer[symbol]))
        list_from_integer.append(string_from_integer[symbol])
    print(list_from_integer)

list_from_integer(initial_num)
