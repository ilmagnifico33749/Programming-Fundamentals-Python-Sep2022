import sys
list_integers = input().split()
num_counts = int(input())

for number in range(num_counts):
    smallest_num = sys.maxsize
    for integer in range(0, len(list_integers)):
        if int(integer) < int(smallest_num):
            smallest_num = list_integers[integer]
    list_integers.remove(smallest_num)
print(", ".join(list_integers))


