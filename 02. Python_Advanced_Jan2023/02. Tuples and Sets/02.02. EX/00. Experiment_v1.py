n, m = ((input()).split(" "))

set_n = {str(input()) for x in range(int(n))}
set_m = {str(input()) for x in range(int(m))}

print('\n'.join(set_n.intersection(set_m)))

# #########
# Input_1:
# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5
# ---------
# Output_1:
# 3
# 5
# #########
# Input_2:
# 2 2
# 1
# 3
# 1
# 5
# ---------
# Output_2:
# 1
# #########
