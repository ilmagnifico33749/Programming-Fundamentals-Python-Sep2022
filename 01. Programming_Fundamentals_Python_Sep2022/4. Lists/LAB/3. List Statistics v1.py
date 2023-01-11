n = int(input())
list_positive_nums = []
list_negative_nums = []
count_positive_nums = 0
sum_negative_nums = 0

for i in range(n):
    number = int(input())
    if number >= 0:
        list_positive_nums.append(number)
        count_positive_nums += 1
    else:
        list_negative_nums.append(number)
        sum_negative_nums += number
print(f"{list_positive_nums}")
print(f"{list_negative_nums}")
print(f"Count of positives: {count_positive_nums}")
print(f"Sum of negatives: {sum_negative_nums}")
