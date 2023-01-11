divisor = int(input())
upper_boundary = int(input())
largest_divisible_num = int()

for num in range(1, upper_boundary + 1, 1):
    if num % divisor == 0 and num != 0:
        largest_divisible_num = num

print(largest_divisible_num)