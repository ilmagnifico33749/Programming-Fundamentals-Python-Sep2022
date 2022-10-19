list_integers = input().split()
num_counts = int(input())
highest_num = int()
for f_num in list_integers:
    if int(f_num) > int(highest_num):
        highest_num = f_num

for counts in range(num_counts):
    smallest_num = highest_num
    for integer in list_integers:
        if int(integer) < int(smallest_num):
            smallest_num = int(integer)
    for element in list_integers:
        if int(element) == smallest_num:
            list_integers.remove(element)
print(", ".join(list_integers))


