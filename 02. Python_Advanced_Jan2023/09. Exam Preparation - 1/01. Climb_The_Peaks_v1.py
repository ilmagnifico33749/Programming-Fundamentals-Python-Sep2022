from _collections import deque

timeframe = 7
dict_peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
daily_food_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(x) for x in input().split(", ")])
list_conquered_peaks = []


for day in range(timeframe):
    # Eventually to break down the below line into once sum and then pop
    daily_energy = daily_food_portions.pop() + daily_stamina.popleft()
    for peak in dict_peaks.keys():
        if dict_peaks[peak] <= daily_energy:
            list_conquered_peaks.append(peak)
            dict_peaks.pop(peak)
            break
        else:
            break

if len(dict_peaks) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
elif len(dict_peaks) > 0:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if list_conquered_peaks:
    print("Conquered peaks:")
    print('\n'.join(list_conquered_peaks))


# ############################################################################
# Input_1:
# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2
# ----------------------------------------------------------------------------
# Output_1:
# Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK
# Conquered peaks:
# Vihren
# Kutelo
# Banski Suhodol
# Polezhan
# Kamenitza
# ############################################################################
# Input_2:
# 10, 20, 34, 26, 12, 10, 45
# 30, 28, 17, 17, 13, 10, 10
# ----------------------------------------------------------------------------
# Output_2:
# Alex failed! He has to organize his journey better next time -> @PIRINWINS
# ############################################################################
