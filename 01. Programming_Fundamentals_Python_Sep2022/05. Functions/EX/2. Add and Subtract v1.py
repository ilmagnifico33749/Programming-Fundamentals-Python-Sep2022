list_all_nums = []

for i in range(3):
    input_number = int(input())
    list_all_nums.append(input_number)

def sum_numbers(number_one, number_two):
    return number_one + number_two

def subtract_nums(sum_one, num_three):
    return sum_one - num_three

def add_and_subtract(num_one, num_two, num_three):
    sum_first_two_nums = sum_numbers(num_one, num_two)
    final_result = subtract_nums(sum_first_two_nums, num_three)
    return final_result

print(add_and_subtract(list_all_nums[0], list_all_nums[1], list_all_nums[2]))