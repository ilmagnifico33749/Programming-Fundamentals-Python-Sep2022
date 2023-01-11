# 2 4 6

list_numbers = input().split(" ")

def list_from_str_to_int(list):
    list_int = []
    for number in list:
        list_int.append(int(number))
    return list_int

def min_num_list(list):
    return min(list)

def max_num_list(list):
    return max(list)

def sum_num_list(list):
    return sum(list)

def final_output(min, max, sum):
    print(f"The minimum number is {min}\nThe maximum number is {max}\nThe sum number is: {sum}")

final_output(min_num_list(list_from_str_to_int(list_numbers)),
             max_num_list(list_from_str_to_int(list_numbers)),
             sum_num_list(list_from_str_to_int(list_numbers)))