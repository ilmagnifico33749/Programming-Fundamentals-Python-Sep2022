user_input = int(input())

def list_divisors_num(number):
    list_divisors = []
    for numbers in range(1, number):
        if number % numbers == 0:
            list_divisors.append(numbers)
    return list_divisors

def aliquot_sum(list_nums):
    return sum(list_divisors_num(user_input))

def validator_perfection(number, sum):
    validity = False
    if number == sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(validator_perfection(user_input, aliquot_sum(list_divisors_num(user_input))))