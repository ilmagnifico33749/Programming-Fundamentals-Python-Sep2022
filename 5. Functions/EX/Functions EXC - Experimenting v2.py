# MyPass123

user_input = int(input())

def list_divisors_num(number):
    list_divisors = []
    for numbers in range(1, number):
        print(numbers)
        if number % numbers == 0:
            list_divisors.append(numbers)
    return list_divisors

print(list_divisors_num(user_input))