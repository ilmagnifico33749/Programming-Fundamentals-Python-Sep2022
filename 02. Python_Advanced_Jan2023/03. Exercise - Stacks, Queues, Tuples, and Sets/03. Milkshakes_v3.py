from _collections import deque

queue_chocolates = deque(int(x) for x in input().split(", "))
queue_cups_milk = deque(int(x) for x in input().split(", "))
count_milkshakes = 0

while count_milkshakes != 5 and queue_chocolates and queue_cups_milk:
    current_chocolate = queue_chocolates.pop()
    current_milk = queue_cups_milk.popleft()

    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        queue_cups_milk.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        queue_chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        count_milkshakes += 1
    else:
        queue_cups_milk.append(current_milk)
        queue_chocolates.append(current_chocolate - 5)

if count_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in queue_chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in queue_cups_milk) or 'empty'}")

# ######################################################
# Input_1:
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
# ------------------------------------------------------
# Output_1:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: 20
# Milk: 10, 55
# ######################################################
# Input_2:
# -10, -2, -30, 10
# -5
# ------------------------------------------------------
# Output_2
# Not enough milkshakes.
# Chocolate: -10, -2, -30, 10
# Milk: empty
# ######################################################
# Input_3:
# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
# ------------------------------------------------------
# Output_3:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: empty
# Milk: 14, 6
# ######################################################
