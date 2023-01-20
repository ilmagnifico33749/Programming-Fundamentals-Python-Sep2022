set_elements = set()

[([set_elements.add(x) for x in input().split(" ")]) for x in range(int(input()))]

print('\n'.join(set_elements))

# ##########
# Input_1:
# 4
# Ce O
# Mo O Ce
# Ee
# Mo
# ----------
# Output_1:
# Ce
# Ee
# Mo
# O
# ##########
# Input_2:
# 3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne
# ----------
# Output_2:
# Ch
# Ge
# Mo
# Nb
# Ne
# O
# Tc
# ##########
