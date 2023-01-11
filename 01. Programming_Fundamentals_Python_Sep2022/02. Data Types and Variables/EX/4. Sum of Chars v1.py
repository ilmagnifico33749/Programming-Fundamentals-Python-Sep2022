num_char = int(input())
sum = 0
for string in range(num_char):
    symbol = input()
    sum += int(ord(symbol))
print(f"The sum equals: {sum}")