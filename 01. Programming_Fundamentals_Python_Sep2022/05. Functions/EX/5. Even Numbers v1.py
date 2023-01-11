# 1 2 3 4

initial_sequence_nums = input().split(" ")
list_sequence_integers = []
for symbol in initial_sequence_nums:
    number_var = int(symbol)
    list_sequence_integers.append(number_var)

def even_nums(number):
    if number % 2 == 0:
        return True
    return False

even_nums_iterator = filter(even_nums, list_sequence_integers)
list_even_nums = list(even_nums_iterator)
print(list_even_nums)