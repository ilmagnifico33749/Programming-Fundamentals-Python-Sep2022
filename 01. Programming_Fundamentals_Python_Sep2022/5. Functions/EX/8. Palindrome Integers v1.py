# 123, 323, 421, 121

initial_list = input().split(", ")

def string_reversal(string):
    reversed_string = string [::-1]
    return reversed_string

def comparison(norm_num, rev_num):
    nums_identicality = False
    if norm_num == rev_num:
        nums_identicality = True
        return "True"
    else:
        return "False"

def final_function(list_nums):
    for number in list_nums:
        print(comparison(number, string_reversal(number)))

final_function(initial_list)