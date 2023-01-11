list_integers = input().split()
num_counts = int(input())
highest_num = int()
for f_num in list_integers:
    if int(f_num) > int(highest_num):
        highest_num = f_num

for number in range(num_counts):
    smallest_num = highest_num
    for integer in range(0, len(list_integers)):
        if int(integer) < int(smallest_num):
            smallest_num = list_integers[integer]
    list_integers.remove(smallest_num)
print(", ".join(list_integers))