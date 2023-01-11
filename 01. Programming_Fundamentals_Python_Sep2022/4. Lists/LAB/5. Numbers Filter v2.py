n = int(input())
list_numbers = []
for lines in range(n):
    number = int(input())
    list_numbers.append(number)
command = str(input())
for i in range(len(list_numbers) -1, -1, -1):
    symbol = int(list_numbers[i])
    if command == "even":
        if symbol % 2 != 0:
            list_numbers.remove(symbol)
    elif command == "odd":
        if symbol % 2 == 0:
            list_numbers.remove(symbol)
    elif command == "negative":
        if symbol >= 0:
            list_numbers.remove(symbol)
    elif command == "positive":
        if symbol < 0:
            list_numbers.remove(symbol)
print(list_numbers)
