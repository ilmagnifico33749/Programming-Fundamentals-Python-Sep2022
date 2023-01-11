counter = 3
list_numbers = []
for count in range(counter):
    number = int(input())
    list_numbers.append(number)

def smallest_num(specific_number):
    return min(list_numbers)

print(smallest_num(list_numbers))