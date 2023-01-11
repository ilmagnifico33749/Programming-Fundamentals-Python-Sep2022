import sys
list_integers = input().split()
num_counts = int(input())

for counts in range(num_counts):
    smallest_num = sys.maxsize
    for integer in list_integers:
        if int(integer) < int(smallest_num):
            smallest_num = int(integer)
    for element in list_integers:
        if int(element) == smallest_num:
            list_integers.remove(element)
print(", ".join(list_integers))


