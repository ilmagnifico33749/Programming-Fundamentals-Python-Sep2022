from collections import deque

ducks_dict = {
    "Darth Vader Ducky": {"Requirements": [0, 60], "Given_Away": 0},
    "Thor Ducky": {"Requirements": [61, 120], "Given_Away": 0},
    "Big Blue Rubber Ducky": {"Requirements": [121, 180], "Given_Away": 0},
    "Small Yellow Rubber Ducky": {"Requirements": [181, 240], "Given_Away": 0}
}

programmers_single_task_time_completion = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]
ducks_max_value = 240

while programmers_single_task_time_completion and number_of_tasks:
    current_programmer_time = programmers_single_task_time_completion[0]
    current_tasks = number_of_tasks[-1]
    current_calculation = current_programmer_time * current_tasks
    if current_calculation > ducks_max_value:
        programmers_single_task_time_completion.append(programmers_single_task_time_completion.popleft())
        number_of_tasks[-1] -= 2
    else:
        for duck, duck_info in ducks_dict.items():
            duck_matched = False
            min_range_duck = duck_info["Requirements"][0]
            max_range_duck = duck_info["Requirements"][1]

            if min_range_duck <= current_calculation <= max_range_duck:
                duck_info["Given_Away"] += 1
                programmers_single_task_time_completion.popleft()
                number_of_tasks.pop()
                break
else:
    print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
    for duck, duck_info in ducks_dict.items():
        print(f"{duck}: {duck_info['Given_Away']}")

# ###################################################
# Test_Code_1:
# 10 15 12 18 22 6
# 12 16 5 6 9 1
# ---------------------------------------------------
# Output_1:
# Congratulations, all tasks have been completed! Rubber ducks rewarded:
# Darth Vader Ducky: 1
# Thor Ducky: 3
# Big Blue Rubber Ducky: 1
# Small Yellow Rubber Ducky: 1
# ###################################################
