import re

regex = "['|'][A-Z]{4}[A-Z]*['|'][:]['#'][a-zA-z]* [a-zA-z]*['#']"

number_inputs = int(input())
for times in range(number_inputs):
    boss_name_validity = False
    filtered = ""
    boss_name = input()
    filtered = re.findall(regex, boss_name)
    if len(filtered) > 0 and filtered[0] == boss_name:
        boss_name_validity = True
        if boss_name_validity == True:
            boss_details = filtered[0].split(":")
            name = boss_details[0][1:(len(boss_details[0])-1)]
            title = boss_details[1][1:(len(boss_details[1])-1)]

            print(f"{name}, The {title}\n>> Strength: {len(name)}\n>> Armor: {len(title)}")
    else:
        print(f"Access denied!")

# (["|"][A-Z]{4}[A-Z]*["|"][:]["#"][a-zA-z]* [a-zA-z]*["#"])
# "(['|'][A-Z]{4}[A-Z]*['|'][:]['#'][a-zA-z]* [a-zA-z]*['#'])"


# 3
# |PETER|:#Lead architect#
# |GEORGE|:#High Overseer#
# |ALEX|:#Assistant Game Developer#
#
# PETER, The Lead architect
# >> Strength: 5
# >> Armor: 14
# GEORGE, The High Overseer
# >> Strength: 6
# >> Armor: 13
# Access denied!


