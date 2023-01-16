### !!! 75/100 in Judge, to verify why

from _collections import deque

deque_combination = deque(x for x in input())

while deque_combination:
    validity = True
    opening_par = deque_combination.popleft()
    closing_par = deque_combination.pop()
    if opening_par == "(" and closing_par == ")":
        continue
    elif opening_par == "{" and closing_par == "}":
        continue
    elif opening_par == "[" and closing_par == "]":
        continue
    else:
        validity = False
        break

if validity == False:
    print("NO")
elif validity == True:
    print("YES")

# #############
# #############
# Input_1:
# {[()]}
# -------------
# Output_1:
# YES
# #############
# Input_2:
# {[(])}
# -------------
# Output_2:
# NO
# #############
# Input_3:
# {{[[(())]]}}
# -------------
# Output_3:
# YES
# #############
# #############
