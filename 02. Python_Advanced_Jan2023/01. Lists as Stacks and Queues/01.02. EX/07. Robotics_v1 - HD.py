from _collections import deque

# robots_info = input().split(";")
robots_info = ["ROB-15", "SS2-10", "NX8000-3"]
# starting_time = input().split(":")
starting_time = ["8", "00", "00"]
queue_products = deque()


command = input()
while command != "End":
     queue_products.append(command)
     command = input()

while queue_products:
    current_time = starting_time


    current_product = queue_products.popleft()


    for robots in range(len(robots_info)):
        print(robots_info[robots])
        robot_details = robots_info[robots].split("-")
        robot_name = robot_details[0]
        robot_handling_time = robot_details[1]




##################
# detail
# glass
# wood
# apple
# End
##################

