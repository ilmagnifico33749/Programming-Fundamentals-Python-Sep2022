my_dict = {}

list_countries = input().split(", ")
list_capitals = input().split(", ")
for number in range(len(list_countries)):
    my_dict[list_countries[number]] = list_capitals[number]
for key in my_dict.keys():
    print(f"{key} -> {my_dict[key]}")

# ------------------------------------#
# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London
# ------------------------------------#
# Bulgaria, Germany, France
# Varna, Frankfurt, Paris
# ------------------------------------#

