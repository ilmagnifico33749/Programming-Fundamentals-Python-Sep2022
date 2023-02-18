from _collections import deque


textiles = [int(x) for x in input().split()]
medicaments = [int(x) for x in input().split()]

my_dict_healing_items = {"Patch": {"Value": 30, "Number": 0},
                         "Bandage": {"Value": 40, "Number": 0},
                         "MedKit": {"Value": 100, "Number": 0}}


def healing_items_creation(list_textiles, list_medicaments, my_dict):
    dict_healing_items = my_dict
    textiles = deque(list_textiles)
    medicaments = list_medicaments
    patch = 30
    bandage = 40
    medkit = 100
    while len(textiles) > 0 and len(medicaments) > 0:
        current_textile = textiles.popleft()
        current_medicament = medicaments.pop()
        sum_textiles_medicament = current_textile + current_medicament
        item_created = False
        for key in dict_healing_items.keys():
            if sum_textiles_medicament == my_dict_healing_items[key]["Value"]:
                my_dict_healing_items[key]["Number"] += 1
                item_created = True
                break
            elif sum_textiles_medicament > my_dict_healing_items["MedKit"]["Value"]:
                my_dict_healing_items["MedKit"]["Number"] += 1
                medicaments[-1] += sum_textiles_medicament - my_dict_healing_items["MedKit"]["Value"]
                item_created = True
                break
            else:
                pass
        if item_created is False:
            medicaments.append(current_medicament + 10)
        return healing_items_creation(textiles, medicaments, dict_healing_items)
    else:
        if len(textiles) == 0 and len(medicaments) != 0:
            print(f"Textiles are empty.")
        elif len(medicaments) == 0 and len(textiles) != 0:
            print(f"Medicaments are empty.")
        elif len(textiles) == 0 and len(medicaments) == 0:
            print(f"Textiles and medicaments are both empty.")

        sorted_dict = dict_healing_items
        for key in sorted_dict.keys():
            del sorted_dict[key]["Value"]
            sorted_dict[key] = sorted_dict[key]['Number']

        sorted_dict = sorted(sorted_dict.items(), key=lambda x: (x[1], x[0]))
        for item in sorted_dict:
            if dict_healing_items[item]['Number'] != 0:
                print(f"{item} - {dict_healing_items[item]['Number']}")
        if textiles:
            print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
        if medicaments:
            print(f"Medicaments left: {', '.join([str(x) for x in sorted(medicaments, reverse=True)])}")


healing_items_creation(textiles, medicaments, my_dict_healing_items)

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
