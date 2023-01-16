### !!! Getting only 20/100 from Judge, to verify why

from _collections import deque

number_petrol_pumps = int(input())
queue_pumps = deque()

for pumps in range(number_petrol_pumps):
    queue_pumps.append(input())

for pump in range(len(queue_pumps)):
    pump_info = queue_pumps.popleft().split(" ")
    pump_petrol_available = int(pump_info[0])
    pump_distance_next_pump = int(pump_info[1])
    if pump_petrol_available >= pump_distance_next_pump:
        print(f"{pump}")
        break

# ###########
# ###########
# Input_1:
# 3
# 1 5
# 10 3
# 3 4
# -----------
# Output_1:
# 1
# ###########
# Input_2:
# 5
# 22 5
# 14 10
# 52 7
# 21 12
# 36 9
# -----------
# Output_2:
# 0
# ###########
# ###########
