from _collections import deque

# robots_info = input().split(";")
robots_info = ["ROB-15", "SS2-10", "NX8000-3"]
# starting_time = input().split(":")
starting_time = ["8", "00", "00"]
queue_products = deque()

def time(starting_time, time_passing_type, time_passing_value):
    starting_time = starting_time.split(":")
    time_passing_type = str(time_passing_type)
    time_passing_value = int(time_passing_value)
    hours = int(starting_time[0])
    minutes = int(starting_time[1])
    seconds = int(starting_time[2])

    if time_passing_type == "seconds":
        seconds += time_passing_value
    elif time_passing_type == "minutes":
        minutes += time_passing_value
    elif time_passing_type == "hours":
        hours += time_passing_value

    if seconds == 60:
        seconds = 00
        minutes += 1
    if minutes == 60:
        minutes = 00
        hours += 1
    if hours == 24:
        hours = 00

    new_hours = str(hours)
    if len(new_hours) == 1:
        new_hours = f"0{new_hours}"
    new_minutes = str(minutes)
    if len(new_minutes) == 1:
        new_minutes = f"0{new_minutes}"
    new_seconds = str(seconds)
    if len(new_seconds) == 1:
        new_seconds = f"0{new_seconds}"

    new_time = f"{new_hours}:{new_minutes}:{new_seconds}"

    return new_time


command = input()
while command != "End":
     queue_products.append(command)
     command = input()

initial_time = "08:00:00"
# print(time(input(), input(), input()))
for times in range(80):
    print(f"Initial Time: {initial_time}")
    # initial_time = "23:59:59"
    new_time = time(initial_time, "seconds", 1)
    print(f"New Time: {new_time}")
    initial_time = new_time
    print(30 * "#")

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

