import sys
eternity = + sys.maxsize

initial_year = int(input())
for year in range(initial_year, eternity, 1):
    current_year = int(year)
    string_current_year = str(year)
    for numbers in range(len(string_current_year)):
        specific_number = string_current_year[numbers]
        if specific_number in range(len(string_current_year)):
            continue
        else:
            print(current_year)
            break
