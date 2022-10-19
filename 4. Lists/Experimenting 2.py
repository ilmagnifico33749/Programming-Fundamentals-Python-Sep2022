list_all_gains = ["1", "2", "3", "4", "5"]
reserve_list_all_gains = ["1", "2", "3", "4", "5"]
number_of_traders = int(input())

list_all_traders = ["Trader 1 gain", "Trader 2 gain", "Trader 3 gain"]

list_final_gains = []
starting_index = 0
while starting_index < number_of_traders:
    gain_current_trader = 0
    for current_index in range(starting_index, len(list_all_gains), number_of_traders):
        gain_current_trader += list_all_gains[current_index]
    list_final_gains.append(gain_current_trader)
    starting_index += 1
print(list_final_gains)






