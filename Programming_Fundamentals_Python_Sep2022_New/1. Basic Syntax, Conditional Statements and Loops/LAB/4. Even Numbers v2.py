n = int(input())
odd_num = int()

for i in range(n):
    a = int(input())
    if a % 2 != 0:
        odd_num = a
        print(f"{odd_num} is odd!")
        break
else:
    print("All numbers are even.")