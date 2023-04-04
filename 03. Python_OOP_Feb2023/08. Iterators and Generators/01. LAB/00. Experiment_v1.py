from collections import deque

my_number = 12345
my_word = "12345"
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
my_deque = deque(my_list)
my_dict = {1: "A", 2: "B", 3: "C", 4: "E", 5: "D"}

print(50 * '#')

print(50 * '-')
# my_iter_1 = iter(my_number) - #TypeError: 'int' object is not iterable
print(50 * '-')

my_iter_2 = iter(my_word)
print(next(my_iter_2))
print(50 * '-')

my_iter_3 = iter(my_list)
print(next(my_iter_3))
print(50 * '-')

my_iter_4 = iter(my_tuple)
print(next(my_iter_4))
print(50 * '-')

my_iter_5 = iter(my_deque)
print(next(my_iter_5))
print(50 * '-')

my_iter_6 = iter(my_dict)
print(next(my_iter_6))
print(50 * '-')

print(50 * '#')

# ----------------------------
# Code representation of the "FOR" loop:

iter_object = iter(my_list)
while True:
    try:
        element = next(iter_object)
        print(element)
    except StopIteration:
        break









