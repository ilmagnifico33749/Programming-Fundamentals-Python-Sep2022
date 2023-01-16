from _collections import deque

food_quantity_day = int(input())
# Template as per Inputs 1 and 2
# food_quantity_day = 348
# food_quantity_day = 499

queue_orders = deque(map(int, input().split()))
# Option_2:
# queue_orders = deque([str(x) for x in input().split()])
# Template as per Inputs 1 and 2
# queue_orders = deque([20, 54, 30, 16, 7, 9])
# queue_orders = deque([57, 45, 62, 70, 33, 90, 88, 76, 100, 50])

print(max(queue_orders))

while food_quantity_day >= 0 and len(queue_orders) > 0:
    current_order = int(queue_orders[0])
    if food_quantity_day >= current_order:
        food_quantity_day -= current_order
        queue_orders.popleft()
    else:
        break

if len(queue_orders) == 0:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join(list(map(str, queue_orders)))}")
    #Option_2:
    # print(f"Orders left: {' '.join([str(x) for x in queue_orders])}")

# ################################
# ################################
# Input_1:
# 348
# 20 54 30 16 7 9
# ---
# Output_1:
# 54
# Orders complete
# ################################
# Input_2:
# 499
# 57 45 62 70 33 90 88 76 100 50
# ---
# Output_2:
# 100
# Orders left: 76 100 50
# ################################
# ################################
