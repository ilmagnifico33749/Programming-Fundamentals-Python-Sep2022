list_all_nums = []
a = ""
for i in range(3):
    input_number = int(input())
    list_all_nums.append(input_number)

def sum_numbers(numbers):
    sum_numbers_var = int(list_all_nums[0]) + int(list_all_nums[1])
    return sum_numbers_var
    #print(sum_numbers_var)

print(sum_numbers(a))

sum_numbers(list_all_nums)
def subtract_nums(num_one, num_two):
    result_subtraction = sum_numbers(a) - list_all_nums[2]
    return result_subtraction

print(subtract_nums(a, a))

def add_and_subtract(sum_res, subt_res):
    final_number = sum_numbers(a) - subtract_nums(a, a)
    return final_number

