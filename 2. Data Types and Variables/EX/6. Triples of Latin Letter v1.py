n = int(input())
for first in range(97, 97+n, 1):
    for second in range(97, 97+n, 1):
        for third in range(97, 97+n, 1):
            print(f"{chr(int(first))}{chr(int(second))}{chr(third)}")