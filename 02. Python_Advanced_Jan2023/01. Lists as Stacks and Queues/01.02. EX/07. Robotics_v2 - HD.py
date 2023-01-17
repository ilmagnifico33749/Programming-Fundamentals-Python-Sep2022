from _collections import deque

robots_info = input().split(";")
starting_time = input()
time_passing_type = "seconds"
time_passing_value = 1
queue_items = deque()
my_dict_robots = {}

# Creating the Dictionary Sections.
for robots in range(len(robots_info)):
    robot_details = robots_info[robots].split("-")
    robot_name = robot_details[0]
    robot_handling_time = robot_details[1]
    my_dict_robots[robot_name] = {}
    my_dict_robots[robot_name]["Handling Time"] = robot_handling_time
    my_dict_robots[robot_name]["Free Status"] = True
    my_dict_robots[robot_name]["Current Task Started at"] = ""
    my_dict_robots[robot_name]["Current Task to Finalize at"] = ""
    my_dict_robots[robot_name]["Currently Handled Item"] = ""
    # my_dict_robots[robot_name]["Previously Handled Items"] = []


# Function for general time calculation.
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

# Creating and filling the Queue with the items to be handled.
command = input()
while command != "End":
    queue_items.append(command)
    command = input()


# The Loop where the magic happens.
current_time = starting_time
while queue_items:
    new_time = time(current_time, time_passing_type, time_passing_value)
    current_item_to_be_handled = queue_items.popleft()

    for key, value in my_dict_robots.items():
        if my_dict_robots[key]["Free Status"] == False:
            if my_dict_robots[key]["Current Task to Finalize at"] == new_time:
                my_dict_robots[key]["Free Status"] = True
                # my_dict_robots[key]["Previously Handled Items"].append(my_dict_robots[key]["Currently Handled Item"])

        if my_dict_robots[key]["Free Status"] == True and current_item_to_be_handled != None:
            my_dict_robots[key]["Currently Handled Item"] = current_item_to_be_handled
            my_dict_robots[key]["Current Task Started at"] = new_time
            my_dict_robots[key]["Current Task to Finalize at"] = time(new_time, time_passing_type, my_dict_robots[key]["Handling Time"])
            my_dict_robots[key]["Free Status"] = False
            print(f"{key} - {current_item_to_be_handled} [{new_time}]")
            current_item_to_be_handled = None

    current_time = new_time
    if current_item_to_be_handled != None:
        queue_items.append(current_item_to_be_handled)

##################################
##################################
# Input_1:
# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End
# --------------------------------
# Output_1:
# ROB - detail [08:00:01]
# SS2 - glass [08:00:02]
# NX8000 - wood [08:00:03]
# NX8000 - apple [08:00:06]
##################################
# Input_2:
# ROB-8
# 7:59:59
# detail
# glass
# wood
# sock
# End
# --------------------------------
# Output_2:
# ROB - detail [08:00:00]
# ROB - wood [08:00:08]
# ROB - glass [08:00:16]
# ROB - sock [08:00:24]
###################################
##################################
