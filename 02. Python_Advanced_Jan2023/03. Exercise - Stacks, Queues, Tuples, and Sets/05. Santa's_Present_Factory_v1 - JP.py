### !!! Getting 70/100 from Judge.

from collections import deque

queue_crafting_materials = deque(int(x) for x in input().split(" "))
queue_magic_level = deque(int(x) for x in input().split(" "))

doll = 150
wooden_train = 250
teddy_bear = 300
bicycle = 400

my_dict_toys = {"Bicycle": 0, "Doll": 0, "Teddy bear": 0, "Wooden Train": 0}

while len(queue_crafting_materials) > 0 and len(queue_magic_level) > 0:
    current_material = int(queue_crafting_materials[-1])
    current_magic = int(queue_magic_level[0])

    if current_material == 0:
        queue_crafting_materials.pop()
    elif current_magic == 0:
        queue_magic_level.popleft()
    else:
        total_magic_level = current_material * current_magic
        if total_magic_level < 0:
            sum_mat_mag = queue_crafting_materials.pop() + queue_magic_level.popleft()
            queue_crafting_materials.append(sum_mat_mag)
        elif total_magic_level > 0:
            if total_magic_level == doll:
                my_dict_toys["Doll"] += 1
                queue_crafting_materials.pop()
                queue_magic_level.popleft()
            elif total_magic_level == wooden_train:
                my_dict_toys["Wooden Train"] += 1
                queue_crafting_materials.pop()
                queue_magic_level.popleft()
            elif total_magic_level == teddy_bear:
                my_dict_toys["Teddy bear"] += 1
                queue_crafting_materials.pop()
                queue_magic_level.popleft()
            elif total_magic_level == bicycle:
                my_dict_toys["Bicycle"] += 1
                queue_crafting_materials.pop()
                queue_magic_level.popleft()
            else:
                queue_magic_level.popleft()
                queue_crafting_materials[-1] = (int(queue_crafting_materials[-1]) + 15)

presents_crafted = False
if my_dict_toys["Doll"] > 0 and my_dict_toys["Wooden Train"] > 0:
    presents_crafted = True
if my_dict_toys["Teddy bear"] > 0 and my_dict_toys["Bicycle"] > 0:
    presents_crafted = True

if presents_crafted is True:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if queue_crafting_materials:
    print(f"Materials left: {', '.join([str(x) for x in queue_crafting_materials][::-1])}")
if queue_magic_level:
    print(f"Magic left: {', '.join([str(x) for x in queue_magic_level])}")

for key, value in my_dict_toys.items():
    if my_dict_toys[key] > 0:
        print(f"{key}: {my_dict_toys[key]}")



# ###
# Input_1:
# 10 -5 20 15 -30 10
# 40 60 10 4 10 0
# ---
# Output_1:
# The presents are crafted! Merry Christmas!
# Materials left: 20, -5, 10
# Bicycle: 1
# Teddy bear: 2
# ###
# Input_2:
# 30 5 15 60 0 30
# -15 10 5 -15 25
# ---
# Output_2:
# No presents this Christmas!
# Materials left: 20, 30
# Doll: 1
# Teddy bear: 1
# ###
# Input_3:
# 30 10
# 15 10 5 0 10
# ---
# Output_3:
# No presents this Christmas!
# Magic left: 5, 0, 10
# Doll: 1
# Teddy bear: 1
# ###
