# 3, 2, 1, 5, 8
list_numbers = list(map(int, input().split(", ")))
list_valid_indices = list(map(lambda x: x if list_numbers[x] % 2 == 0 else "NOT", range(len(list_numbers))))
final_list_indices = list(filter(lambda x: x != "NOT", list_valid_indices))
print(final_list_indices)