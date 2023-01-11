# 1000435

initial_num = int(input())

def list_from_integer(integer):
    string_from_integer = str(integer)
    list_from_integer = []
    for symbol in range(len(string_from_integer)):
        list_from_integer.append(string_from_integer[symbol])
    return list_from_integer

def filtering_function(list_numbers):
    list_even_nums = []
    list_odd_nums = []
    for symbols in list_numbers:
        print(symbols)
        if int(symbols) % 2 == 0:
            list_even_nums.append(int(symbols))
        elif int(symbols) % 2 != 0:
            list_odd_nums.append(int(symbols))
    print(f"Odd sum = {sum(list_odd_nums)}, Even sum = {sum(list_even_nums)}")

filtering_function(list_from_integer(initial_num))