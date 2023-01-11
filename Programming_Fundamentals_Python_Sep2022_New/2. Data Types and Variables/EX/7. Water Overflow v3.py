tank_capacity = 255
lines = int(input())
total_water = 0
for i in range(lines):
    litres_once = int(input())
    pot_new_fill = tank_capacity - litres_once
    if pot_new_fill >= 0:
        tank_capacity -= litres_once
        total_water += litres_once
    else:
        print(f"Insufficient capacity!")
print(total_water)
