import math

def get_primes(numbers):
    for number in numbers:
        if number <= 1:
            continue

        for num in range(2, int(math.sqrt(number)) + 1):
            if number % num == 0:
                break
        else:
            yield number


# ##################################
# Test_Code_1:
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
# ---------------------------------
# Output_1:
# [2, 3, 5]
# ##################################
# Test_Code_2:
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
# ---------------------------------
# Output_2:
# []
# ##################################
