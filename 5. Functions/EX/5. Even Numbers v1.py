
# 1 2 3 4

initial_sequence_nums = input()

def list_from_sequence_symbols(integer):
    list_symbols = integer.split(" ")
    return list_symbols

def filtering_even_nums(list_number):
    list_even_nums = []
    for number in list_number:
        if int(number) % 2 == 0:
            list_even_nums.append(number)
    return list_even_nums

print(filtering_even_nums(list_from_sequence_symbols(initial_sequence_nums)))