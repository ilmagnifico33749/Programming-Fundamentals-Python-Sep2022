integer = 1000435
list_from_integer = []
print(f"Len Integer: {len(str(integer))}")
a = str(integer)
for symbol in range(len(a)):
    print(f"Symbol: {symbol}")
    print(str(a[symbol]))
    b = int(a[symbol])
    list_from_integer.append(b)
print(list_from_integer)
print(sum(list_from_integer))
