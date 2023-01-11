n = float(input())
within_range = False

while within_range == False:
    while n < 1 or n > 100:
        n = float(input())
        pass
    else:
        within_range = True
        print(f"The number {n} is between 1 and 100")
        break
