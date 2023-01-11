tank_capacity = 255
capacity_filled = 0
lines = int(input())
for i in range(lines):
    litres_once = int(input())
    pot_cap_fill = capacity_filled + litres_once
    if pot_cap_fill < tank_capacity:
        capacity_filled += litres_once
    else:
        print(f"Insufficient capacity!")
print(capacity_filled)
