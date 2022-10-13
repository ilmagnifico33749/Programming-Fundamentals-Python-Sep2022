n = int(input())
for first in range(0, n):
    for second in range(0, n):
        for third in range(0, n):
            print(f"{chr(int(97 + first))}{chr(int(97 + second))}{chr(97 + third)}")