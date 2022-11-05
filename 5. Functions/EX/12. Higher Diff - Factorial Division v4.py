def factorial(number):
    sum_nums = 1
    for numbers in range(1, number + 1):
        sum_nums *= numbers
    return sum_nums

factorial_division = lambda factorial_one, factorial_two: factorial_one / factorial_two

print(f"{factorial_division(factorial(int(input())), factorial(int(input()))):.2f}")