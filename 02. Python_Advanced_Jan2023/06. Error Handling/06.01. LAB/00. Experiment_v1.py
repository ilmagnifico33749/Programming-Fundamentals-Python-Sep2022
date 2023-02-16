def sum_even_numbers(nums):
    even_numbers = 0

    for num in nums:
        if num % 2 == 0:
            even_numbers += num
        elif num % 2 != 0:
            continue
        else:
            raise ValueError
    print(even_numbers)

try:
    # sum_even_numbers(["8", 5, 6])
    sum_even_numbers([8, 5, 6])

except:
    print("Exception Handled")

finally:
    print(f"Finally")



