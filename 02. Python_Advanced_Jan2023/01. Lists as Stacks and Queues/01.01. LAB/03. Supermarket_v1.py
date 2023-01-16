from collections import deque

my_queue = deque()

command = input()

while command != "End":
    if command != "Paid":
        my_queue.append(command)
    else:
        while my_queue:
            print(my_queue.popleft())

    command = input()

else:
    print(f"{len(my_queue)} people remaining.")

# ##########################
# Input_1:
# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End
# --------------------------
# Output_1:
# George
# Peter
# William
# 4 people remaining.
# ##########################
# Input_2:
# Anna
# Emma
# Alexander
# End
# --------------------------
# Output_2:
# 3 people remaining.
# ##########################
