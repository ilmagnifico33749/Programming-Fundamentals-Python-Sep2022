integer_one = int(input())
integer_two = int(input())

def factorial(number):
    sum_nums = 1
    for numbers in range(1, number + 1):
        sum_nums *= numbers
    return sum_nums

factorial_division = lambda factorial_one, factorial_two: factorial_one / factorial_two
print(f"{factorial_division(factorial(integer_one), factorial(integer_two)):.2f}")