# 8, 12, 38, 3, 17, 19, 25, 35, 50
# 1, 3, 3, 4, 34, 35, 25, 21, 33

user_input = list(map(int, input().split(", ")))
lower_range = -10
higher_range = 0

def grouping(low_range, high_range, list):
    max_num_list = max(list)
    while True:
        if low_range < max_num_list > high_range:
            low_range += 10
            high_range = low_range + 10
            new_list = []
            [new_list.append(list[x]) for x in range(len(list)) if low_range < list[x] <= high_range]
            print(f"Group of {high_range}': {new_list}")

grouping(lower_range, higher_range, user_input)