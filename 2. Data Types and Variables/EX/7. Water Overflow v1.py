tank_capacity = 255
capacity_filled = 0
lines = int(input())
for i in range(lines):
    litres_once = int(input())
    if capacity_filled < tank_capacity:
        if (capacity_filled + litres_once) < tank_capacity:
                capacity_filled += capacity_filled
        else:
            print(f"Insufficient capacity!\n{print(capacity_filled)}")
            break
print(capacity_filled)


