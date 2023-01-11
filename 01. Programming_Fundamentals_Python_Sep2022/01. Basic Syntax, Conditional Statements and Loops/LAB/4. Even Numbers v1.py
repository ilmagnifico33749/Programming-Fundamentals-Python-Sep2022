n = int(input())
all_numbers_even = True
odd_number = int()

for i in range(n):
    a = int(input())
    if a % 2 == 0:
        pass
    else:
        all_numbers_even = False
        odd_number = a
        break

if all_numbers_even == True:
    print("All numbers are even.")
else:
    print(f"{odd_number} is odd!")
