list_all_gains = ["1", "2", "3", "4", "5"]
copy_list_all_gains = list_all_gains
list_all_traders = ["Trader 1 gain", "Trader 2 gain", "Trader 3 gain"]
list_individual_gains_trader = []

while len(list_all_gains) > 0:
    for trader in list_all_traders:
        gain = int(list_all_gains[0])
        print(f"Gain: {gain}")
        list_individual_gains_trader.append(list_all_gains[0])
        list_all_gains.remove(list_all_gains[0])













