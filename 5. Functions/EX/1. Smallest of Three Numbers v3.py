counter = 3
list_numbers = []
for count in range(counter):
    number = int(input())
    list_numbers.append(number)

smallest_num = lambda list_one: min(list_one)
print(smallest_num(list_numbers))