n = int(input())
for a in range(1, n+1):
    print(int(a) * "*")
for b in range(n-1, 0, -1):
    print(int(abs(b)) * "*")

