# 3, 2, 1, 5, 8
list_numbers = list(map(int, input().split(", ")))
final_list_indices = list(filter(lambda x: x != "NOT", list(map(lambda x: x if list_numbers[x] % 2 == 0 else "NOT", range(len(list_numbers))))))
print(final_list_indices)