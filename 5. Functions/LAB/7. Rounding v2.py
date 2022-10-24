list_floats = input().split(" ")
list_round_numbers = []

def rounding(number):
    for number in list_floats:
        round_number = round(float(number))
        list_round_numbers.append(round_number)
    return list_round_numbers

print(rounding(list_floats))
