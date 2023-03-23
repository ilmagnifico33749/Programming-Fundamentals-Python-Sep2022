import re

list_furniture = []
command = input()
total_expenses = 0
regex = ">>([a-zA-Z]+)<<([0-9]+[.|,]*[0-9]*)!([0-9]+)"
total_budget = 0

while command != "Purchase":
    matches = re.finditer(regex, command)
    command = input()
    for match in matches:
        furniture_name = str(match.group(1))
        price_per_unit = float(match.group(2))
        number_of_units = float(match.group(3))
        total_cost = price_per_unit * number_of_units
        list_furniture.append(furniture_name)
        total_budget += total_cost
else:
    result = "Bought furniture:\n"
    for item in list_furniture:
        result += f"{item}\n"
    result += str(f"Total money spend: {total_budget:.2f}")

print(result)
# valid_format = ">>{furniture_name}<<{price}!{quantity}


###############################
# Input_1:
# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
##############################
# Output_1:
# Bought furniture:
# Sofa
# TV
# Total money spend: 2436.69
##############################
