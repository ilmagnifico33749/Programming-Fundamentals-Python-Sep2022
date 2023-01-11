def sum_numbers(number_one, number_two):
    return number_one + number_two

def subtract_nums(sum_one, num_three):
    return sum_one - num_three

def add_and_subtract(num_one, num_two, num_three):
    sum_first_two_nums = sum_numbers(num_one, num_two)
    final_result = subtract_nums(sum_first_two_nums, num_three)
    return final_result

num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_subtract(num_one, num_two, num_three))