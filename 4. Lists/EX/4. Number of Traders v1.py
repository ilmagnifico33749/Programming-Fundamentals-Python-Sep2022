list_all_gains = input().split(", ")
print(list_all_gains)
print(list_all_gains[0])
copy_list_all_gains = list_all_gains
number_of_traders = int(input())
list_all_traders = []
first_list_all_gains_per_trader = []


for all_traders in range(1, number_of_traders + 1):
    first_list_all_gains_per_trader.append(f"Trader {all_traders} gain")

while len(list_all_gains) > 0:
    for trader in first_list_all_gains_per_trader:
        list_trader_gain_day = []
        list_trader_gain_day.append(trader)
        for daily_gain_per_trader in list_all_gains:
            print(f"Daily gain per trader {daily_gain_per_trader}")
            list_trader_gain_day.append(daily_gain_per_trader)
            list_all_gains.remove(daily_gain_per_trader)
        print(list_trader_gain_day)












