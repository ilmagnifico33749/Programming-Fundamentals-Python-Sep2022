list_all_gains = input().split(", ")
number_of_traders = int(input())

list_all_gains_integers = []
for element in list_all_gains:
    list_all_gains_integers.append(int(element))

list_final_gains = []
starting_index = 0
while starting_index < number_of_traders:
    gain_current_trader = 0
    for current_index in range(starting_index, len(list_all_gains), number_of_traders):
        gain_current_trader += list_all_gains_integers[current_index]
    list_final_gains.append(gain_current_trader)
    starting_index += 1
print(list_final_gains)












