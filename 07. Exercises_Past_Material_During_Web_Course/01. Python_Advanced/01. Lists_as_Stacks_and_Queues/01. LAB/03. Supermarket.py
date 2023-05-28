from collections import deque

customers = deque()

command = input()
while command != "End":
    if command != "Paid":
        customers.append(command)
    else:
        while customers:
            print(customers.popleft())
    command = input()
else:
    print(f"{len(customers)} people remaining.")

#
#
# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End

# Anna
# Emma
# Alexander
# End