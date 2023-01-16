from collections import deque

list_players = list(input().split(" "))
queue_players = deque(list_players)
fatal_toss = int(input())

while len(queue_players) > 1:
    for tosses in range(1, fatal_toss):
            queue_players.append(queue_players.popleft())
    print(f"Removed {queue_players.popleft()}")

else:
    print(f"Last is {''.join(queue_players)}")

# ######################################
# ######################################
# Input_1:
# Tracy Emily Daniel
# 2
# -----------------------------------
# Output_1:
# Removed Emily
# Removed Tracy
# Last is Daniel
# ######################################
# Input_2:
# George Peter Michael William Thomas
# 10
# -----------------------------------
# Output_2:
# Removed Thomas
# Removed Peter
# Removed Michael
# Removed George
# Last is William
# ######################################
# Input_3:
# George Peter Michael William Thomas
# 1
# -----------------------------------
# Output_3:
# Removed George
# Removed Peter
# Removed Michael
# Removed William
# Last is Thomas
# ######################################
# ######################################
