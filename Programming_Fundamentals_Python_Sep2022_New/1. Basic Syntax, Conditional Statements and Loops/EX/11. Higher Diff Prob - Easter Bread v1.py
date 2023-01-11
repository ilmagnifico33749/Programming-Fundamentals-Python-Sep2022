total_budget_available = float(input())
flour_price_kg = float(input())
flour_per_loaf = flour_price_kg * 1
eggs_price_pack = flour_price_kg * 0.75
eggs_per_loaf = eggs_price_pack * 1
milk_per_loaf = (flour_per_loaf * 1.25) * 0.25
budget_per_loaf = flour_per_loaf + eggs_per_loaf + milk_per_loaf
bread_count = 0
colored_eggs_count = 0
while total_budget_available >= budget_per_loaf:
    total_budget_available -= budget_per_loaf
    bread_count += 1
    colored_eggs_count += 3
    if bread_count % 3 == 0:
        colored_eggs_count -= bread_count - 2

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs "
      f"and {total_budget_available:.2f}BGN left.")