year = int(input())
happy_year = False

while happy_year == False:
    year += 1
    year_set = {year}
    if len(year_set) == len(year):
        print(year)
        break

