from collections import deque

textiles = deque([int(x) for x in input().split(" ")])
medicaments = [int(x) for x in input().split(" ")]

dict_healing_items_req = {"Patch": 30, "Bandage": 40, "MedKit": 100}
dict_healing_items_created = {"Patch": 0, "Bandage": 0, "MedKit": 0}

def creator_heal_item(array_textiles, array_medicaments):
    textile_value = textiles.popleft()
    medicament_value = medicaments.pop()
    sum_textile_medicament = textile_value + medicament_value
    for key, value in dict_healing_items_req.items():
        if value == sum_textile_medicament:
            dict_healing_items_created[key] += 1
            return
        elif key == "MedKit":
            if sum_textile_medicament > value:
                dict_healing_items_created[key] += 1
                medicaments[-1] += (sum_textile_medicament - value)
                return
        else:
            pass
    medicaments.append(medicament_value+10)
    return

while textiles and medicaments:
    creator_heal_item(textiles, medicaments)
else:
    if not textiles and not medicaments:
        print(f"Textiles and medicaments are both empty.")
    else:
        if not textiles: print("Textiles are empty.")
        if not medicaments: print("Medicaments are empty.")


sorted_dict_items_created = sorted(dict_healing_items_created.items(), key=lambda x: (-x[1], x[0]))

for item_details in sorted_dict_items_created:
    item_name, item_value = item_details[0], item_details[1]
    if item_value > 0:
        print(f"{item_name} - {item_value}")

if textiles: print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
if medicaments: print(f"Medicaments left: {', '.join(reversed([str(x) for x in medicaments]))}")


# ########################################################
# Input_1:
# 20 10 40 70 20
# 10 50 10 30 20 80
# --------------------------------------------------------
# Output_1:
# Textiles are empty.
# MedKit - 2
# Bandage - 1
# Patch - 1
# Medicaments left: 50, 10
# ########################################################
# Input_2:
# 30 30 10 80 60
# 40 20 30 10 70
# --------------------------------------------------------
# Output_2:
# Textiles and medicaments are both empty.
# MedKit - 3
# Bandage - 2
# ########################################################
# Input_3:
# 30 30 10 80 60 20
# 40 20 30 10 70
# --------------------------------------------------------
# Output_3:
# Medicaments are empty.
# MedKit - 3
# Bandage - 2
# Textiles left: 20
# ########################################################
# Input_4:
# 60 15 20 30 20
# 20 15 40
# --------------------------------------------------------
# Output_4:
# Medicaments are empty.
# Bandage - 1
# MedKit - 1
# Patch - 1
# Textiles left: 30, 20
# ########################################################
