list_integers = []
for number in range(2):
    user_input = int(input())
    list_integers.append(user_input)

def factorial(number):
    sum_nums = 1
    for numbers in range(1, number + 1):
        sum_nums *= numbers
    return sum_nums

factorial_division = lambda factorial_one, factorial_two: factorial_one / factorial_two
print(f"{factorial_division(factorial(list_integers[0]), factorial(list_integers[1])):.2f}")