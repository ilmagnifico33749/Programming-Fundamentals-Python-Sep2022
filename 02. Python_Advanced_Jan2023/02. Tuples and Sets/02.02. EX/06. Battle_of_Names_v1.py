number_of_names = int(input())

set_even = set()
set_odd = set()

for names in range(1, number_of_names + 1):
    sum_letter_name = int(sum([ord(x) for x in input()]) / names)
    if sum_letter_name % 2 == 0:
        set_even.add(sum_letter_name)
    elif sum_letter_name % 2 == 1:
        set_odd.add(sum_letter_name)

set_even_sum = sum(set_even)
set_odd_sum = sum(set_odd)

if set_even_sum == set_odd_sum:
    print(', '.join(map(str, set_even.union(set_odd))))
elif set_even_sum < set_odd_sum:
    print(', '.join(map(str, set_odd.difference(set_even))))
elif set_even_sum > set_odd_sum:
    print(', '.join(map(str, set_even.symmetric_difference(set_odd))))

# ####################
# Input_1:
# 4
# Pesho
# Stefan
# Stamat
# Gosho
# --------------------
# Output_1:
# 304, 128, 206, 511
# ####################
# Input_2:
# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan
# --------------------
# Output_2:
# 733, 101
# ####################
