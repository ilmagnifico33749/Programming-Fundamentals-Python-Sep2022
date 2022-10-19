import sys
list_integers = input().split()
num_counts = int(input())

for number in range(num_counts):
    smallest_num = sys.maxsize
    for integer in list_integers:
        if int(integer) < int(smallest_num):
            smallest_num = int(integer)
    list_integers.remove(str(smallest_num))
print(", ".join(list_integers))