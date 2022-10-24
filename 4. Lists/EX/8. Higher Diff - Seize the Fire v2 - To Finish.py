#Rework the below using the bool as conditional statement

initial_list_all_fires = input().split("#")
fire_validity = True
initial_amount_water = int(input())
current_amount_of_water = initial_amount_water
water_left_after_fire = initial_amount_water
list_fires_put_out = ['Cells:']
total_fire_put_out = 0
total_effort = 0

for fires in initial_list_all_fires:
    fire = fires.split(" = ")
    if fire[0] == "High":
        if 81 <= int(fire[1]) <= 125:
            fire_validity = True
            water_left_after_fire -= (1.25 * int(fire[1]))
            if water_left_after_fire >= 0:
                current_amount_of_water -= water_left_after_fire
                total_fire_put_out += int(fire[1])
                total_effort += (int(fire[1]) * 0.25)
                list_fires_put_out.append(str(fire[1]))
        else:
            fire_validity = False
            pass
    if fire[0] == "Medium":
        if 51 <= int(fire[1]) <= 80:
            fire_validity = True
            water_left_after_fire -= (1.25 * int(fire[1]))
            if water_left_after_fire >= 0:
                current_amount_of_water -= water_left_after_fire
                total_fire_put_out += int(fire[1])
                total_effort += (int(fire[1]) * 0.25)
                list_fires_put_out.append(str(fire[1]))
        else:
            fire_validity = False
            pass
    if fire[0] == "Low":
        if 1 <= int(fire[1]) <= 50:
            fire_validity = True
            water_left_after_fire -= (1.25 * int(fire[1]))
            if water_left_after_fire >= 0:
                current_amount_of_water -= water_left_after_fire
                total_fire_put_out += int(fire[1])
                total_effort += (int(fire[1]) * 0.25)
                list_fires_put_out.append(str(fire[1]))
            else:
                pass
        else:
            fire_validity = False
print("\n - ".join(list_fires_put_out))
print(f"Effort: {total_effort}\nTotal Fire: {total_fire_put_out}")