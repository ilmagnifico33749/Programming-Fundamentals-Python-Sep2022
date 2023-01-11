# 8, 12, 38, 3, 17, 19, 25, 35, 50
# 1, 3, 3, 4, 34, 35, 25, 21, 33

user_input = list(map(int, input().split(", ")))
max_num_list = max(user_input)
lower_range = -10
higher_range = 0

while True:
    if lower_range < max_num_list > higher_range:
        lower_range += 10
        higher_range = lower_range + 10
        new_list = []
        [new_list.append(user_input[x]) for x in range(len(user_input)) if lower_range < user_input[x] <= higher_range]
        print(f"Group of {higher_range}': {new_list}")



