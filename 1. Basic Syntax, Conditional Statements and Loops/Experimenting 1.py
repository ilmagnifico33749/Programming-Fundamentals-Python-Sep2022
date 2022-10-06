#a = input()
#print(ord(a))
#print(chr(97))
#new_command = ""

total_budget_available = input()
flour_price_kg = input()
flour_per_loaf = flour_price_kg * 1
eggs_price_pack = float(flour_price_kg) * 0.75
eggs_per_loaf = float(eggs_price_pack) * 1
milk_per_loaf = float(float((flour_per_loaf * 1.25)) * 0.25)
budget_per_loaf = float(flour_per_loaf) + float(eggs_per_loaf) + float(milk_per_loaf)
bread_count = 0
colored_eggs_count = 0
while total_budget_available >= budget_per_loaf:
    total_budget_available -= budget_per_loaf
    bread_count += 1
    colored_eggs_count += 3
    if bread_count % 3 == 0:
        colored_eggs_count -= bread_count - 2


print(f"You made {loaves_capacity} loaves of Easter bread! Now you have {coloured_eggs_count} /"
      f"and {money_left:.2f} BGN left ")

