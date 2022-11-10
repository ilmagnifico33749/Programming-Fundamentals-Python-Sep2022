# input_1: 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
# output_1:
#           Positive: 1, 0, 5, 3, 4, 12, 19
#           Negative: -2, -100, -20, -33
#           Even: -2, 0, 4, -100, -20, 12
#           Odd: 1, 5, 3, 19, -33
# input_2: 1, 2, 53, 2, 21
# output_2:
#           Positive: 1, 2, 53, 2, 21
#           Negative:
#           Even: 2, 2
#           Odd: 1, 53, 21

list_user_input = input().split(", ")
print(f"Positive: {', '.join([x for x in list_user_input if int(x) >= 0])}")
print(f"Negative: {', '.join([x for x in list_user_input if int(x) < 0])}")
print(f"Even: {', '.join([x for x in list_user_input if int(x) % 2 == 0])}")
print(f"Odd: {', '.join([x for x in list_user_input if int(x) % 2 != 0])}")