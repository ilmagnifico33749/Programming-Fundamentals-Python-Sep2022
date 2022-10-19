import sys
list_integers = ['1', '10', '2', '9', '3', '8']
num_counts = 2


for number in range(num_counts):
    smallest_num = sys.maxsize
    for integer in list_integers:
        print(f"Integer: {integer}")
        if int(integer) < int(smallest_num):
            smallest_num = int(integer)
            print(f"Smallest Number: {smallest_num}")
        list_integers.remove(smallest_num)
    print(f"Removing: {integer}")
print(", ".join(list_integers))


