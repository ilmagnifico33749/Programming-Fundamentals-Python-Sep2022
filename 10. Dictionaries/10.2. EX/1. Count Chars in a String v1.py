#----------------------------#
# input_1: text
# output_1:
# t -> 2
# e -> 1
# x -> 1
#----------------------------#
# input_2: text text text
# output_2:
# t -> 6
# e -> 3
# x -> 3
#----------------------------#

my_dict = {}

list_user_input = [x for x in input()]
for letter in list_user_input:
    if ord(letter) != 32:
        my_dict[letter] = list_user_input.count(letter)
for key in my_dict.keys():
    print(f"{key} -> {my_dict[key]}")
