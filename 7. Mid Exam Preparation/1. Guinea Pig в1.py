food_quan = float(input()) * 1000
hay_quant = float(input()) * 1000
cover_quan = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000

count_days = 0
for days in range(30):
    count_days += 1
    food_quan -= 300
    enough_food = True

    if food_quan <= 0 or hay_quant <= 0 or cover_quan <= 0:
        enough_food = False
        print(f"Merry must go to the pet store!")
        break
    else:
        if count_days % 2 == 0:
            hay_quant -= (food_quan * 0.05)
        if count_days % 3 == 0:
            cover_quan -= (guinea_pig_weight / 3)

if enough_food == True:
    print(f"Everything is fine! Puppy is happy! Food: {(food_quan/1000):.2f}, Hay: {(hay_quant/1000):.2f}, Cover: {(cover_quan/1000):.2f}.")

