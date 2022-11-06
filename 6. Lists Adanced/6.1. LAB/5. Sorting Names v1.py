# Ali, Marry, Kim, Teddy, Monika, John
original_list_names = input().split(", ")
new_sorted_list_one = sorted(original_list_names, key=lambda name: (-len(name)))
print(new_sorted_list_one)

# Ali, Marry, Kim, Teddy, Monika, John, 1, a,  , ., #, !
#new_sorted_list_two = sorted(original_list_names)
#print(new_sorted_list_two)
