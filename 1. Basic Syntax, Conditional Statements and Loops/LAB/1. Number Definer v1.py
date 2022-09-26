a = float(input())

if a == 0:
    print("zero")
elif a >= 0:
    if 1 <= abs(a) <= 1000000:
        print("positive")
    elif abs(a) < 1:
        print("small positive")
    elif abs(a) > 1000000:
        print("large positive")

elif a < 0:
    if 1 <= abs(a) <= 1000000:
        print("negative")
    elif abs(a) < 1:
        print("small negative")
    elif abs(a) > 1000000:
        print("large negative")