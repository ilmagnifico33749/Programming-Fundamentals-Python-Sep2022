list_items = input().split(", ")
command = input()

while command != "Craft!":
    command_details = command.split(" - ")
    instruction = command_details[0]
    item = command_details[1]

    if instruction == "Collect":
        if item in list_items:
            pass
        else:
            list_items.append(item)
    elif instruction == "Drop":
        if item in list_items:
            list_items.remove(item)
    elif instruction == "Renew":
        if item in list_items:
            list_items.remove(item)
            list_items.append(item)
    elif instruction == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in list_items:
            for item_current in range(len(list_items)):
                if list_items[item_current] == old_item:
                    list_items.insert((int(item_current) + 1), new_item)

    command = input()

else:
    print(", ".join(list_items))

# ----------------------------#
# Input_1:
# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!
#
# Output_1:
# Iron, Sword, Gold
# ----------------------------#
# Input_2:
# Iron, Sword
# Drop - Bronze
# Combine Items - Sword:Bow
# Renew - Iron
# Craft!
#
# Output_2:
# Sword, Bow, Iron
# ----------------------------#

