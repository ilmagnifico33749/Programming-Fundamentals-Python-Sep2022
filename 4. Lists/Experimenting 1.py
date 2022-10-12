n = int(input())
list_numbers = []
for lines in range(n):
    number = int(input())
    list_numbers.append(number)
for i in range(len(list_numbers) -1, -1, -1):
    symbol = int(list_numbers[i])
    print(symbol)
