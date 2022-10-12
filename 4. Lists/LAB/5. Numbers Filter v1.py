# !!! There seems to be some bug in Python or the list íterating or something I'm missing
#When the input is the below and the iterating cycle is "for symbol in list_numbers:" it's not
# iterating through the number "19". To investigate further!:
#5
#33
#19
#-2
#18
#998
#even

n = int(input())
list_numbers = []
for lines in range(n):
    number = int(input())
    list_numbers.append(number)
command = str(input())
for symbol in list_numbers:
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
