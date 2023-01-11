#-----------------------------------------#
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards
#-----------------------------------------#
# 123 silver 6 shards 8 shards 5 motes
# 9 fangs 75 motes 103 MOTES 8 Shards
# 86 Motes 7 stones 19 silver
#-----------------------------------------#

my_dict_legendary = {"key_materials": {"shards": 0, "fragments": 0, "motes": 0}, "junk": {}}

item_found = False
enough_obtained_from = ""
while True:
    while item_found == False:
        command_details = input().split(" ")
        list_material = [str(command_details[x]).lower() for x in range(1, len(command_details), 2)]
        list_quantity = [int(command_details[x]) for x in range(0, len(command_details), 2)]
        for item in range(len(list_material)):
            item_key = list_material[item]
            item_value = int(list_quantity[item])
            if item_key == "shards" or item_key == "fragments" or item_key == "motes":
                my_dict_legendary["key_materials"][item_key] += int(item_value)
                if my_dict_legendary["key_materials"][item_key] >= 250:
                    my_dict_legendary["key_materials"][item_key] -= 250
                    item_found = True
                    enough_obtained_from = item_key
                    break
            elif item_key != "shards" or item_key != "fragments" or item_key != "motes":
                if item_key in my_dict_legendary["junk"].keys():
                    my_dict_legendary["junk"][item_key] += item_value
                else:
                    new_value = {str(item_key): int(item_value)}
                    my_dict_legendary["junk"][item_key] = item_value
    else:
        if enough_obtained_from == "shards":
            print(f"Shadowmourne obtained!")
        elif enough_obtained_from == "fragments":
            print(f"Valanyr obtained!")
        elif enough_obtained_from == "motes":
            print(f"Dragonwrath obtained!")
        for main_key in my_dict_legendary.keys():
            for secondary_key in my_dict_legendary[main_key].keys():
                print(f"{secondary_key}: {my_dict_legendary[main_key][secondary_key]}")
        break
