a = float(input())
value = ""
number_size = ""
if a == 0:
    value = "zero"
elif a > 0:
    value = "positive"
elif a < 0:
    value = "negative"

if abs(a) < 1 and abs(a) != 0:
    number_size = "small"
elif abs(a) > 1000000 and abs(a) != 0:
    number_size = "large"

print(f"{number_size} {value}")