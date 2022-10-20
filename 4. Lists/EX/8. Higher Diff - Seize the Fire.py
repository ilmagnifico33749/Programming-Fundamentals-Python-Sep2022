initial_list_all_fires = input().split("#")
print(initial_list_all_fires)
fire_validity = True
initial_amount_water = int(input())
current_amount_of_water = int(input())

for fires in initial_list_all_fires:
    fire = fires.split(" = ")
    if fire[0] == "High":
        if 81 <= fire[1] <= 125:
            fire_validity = True
            current_amount_of_water -= (1.25 * fire[1])
        else:
            fire_validity = False
            pass
    if fire[0] == "Medium":
        if 51 <= fire[1] <= 80:
            fire_validity = True
            current_amount_of_water -= (1.25 * fire[1])
        else:
            fire_validity = False
            pass
    if fire[0] == "Low":
        if 1 <= fire[1] <= 50:
            fire_validity = True
            current_amount_of_water -= (1.25 * fire[1])
        else:
        fire_validity = False






