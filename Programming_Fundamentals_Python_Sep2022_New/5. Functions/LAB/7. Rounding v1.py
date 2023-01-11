list_floats = input().split(" ")
list_round_numbers = []

def rounding(number):
    for number in list_floats:
        round_number = round(float(number))
        list_round_numbers.append(round_number)
    print(list_round_numbers)

rounding(list_floats)
