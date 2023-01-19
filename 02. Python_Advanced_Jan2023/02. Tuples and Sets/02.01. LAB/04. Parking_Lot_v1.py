commands_number = int(input())
parked_cars = set()
for cars in range(commands_number):
    direction, car_plate = input().split(", ")
    if direction == "IN" and car_plate not in parked_cars:
        parked_cars.add(car_plate)
    elif direction == "OUT" and car_plate in parked_cars:
        parked_cars.remove(car_plate)

if len(parked_cars) == 0:
    print(f"Parking Lot is Empty")
else:
    [print(x) for x in parked_cars]

# ###############
# Input_1:
# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU
# --------------
# Output_1
# CA2844AA
# CA9999TT
# CA2822UU
# CA9876HH
# ###############
# Input_2:
# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA
# --------------
# Output_2:
# Parking Lot is Empty
# ###############
