from _collections import deque

water_available = int(input())
my_queue_1_people = deque()
command = input()

while command != "Start":
    my_queue_1_people.append(command)
    command = input()
else:
    for person in range(len(my_queue_1_people)):
        command_two = input()
        while command_two != "End":
            command_details = command_two.split()
            if len(command_details) == 1:
                water_to_consume = int(command_details[0])
                if water_to_consume <= water_available:
                    water_available -= water_to_consume
                    print(f"{my_queue_1_people.popleft()} got water")
                else:
                    print(f"{my_queue_1_people.popleft()} must wait")
            elif len(command_details) == 2:
                if command_details[0] == "refill":
                    water_available += int(command_details[1])
            command_two = input()
        else:
            print(f"{water_available} liters left")
            break

# ######################
# Input_1:
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End
# ---------------------
# Output_1:
# Peter got water
# Amy got water
# 0 liters left
# ######################
# Input_2:
# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End
# ---------------------
# Output_2:
# Peter got water
# George got water
# Amy got water
# Alice must wait
# 2 liters left
# ######################
