list_employees_happiness = list(map(int, (input().split(" "))))
happiness_factor = int(input())
print(list_employees_happiness)
factor_list_employees_happiness = list(map((lambda x: x * happiness_factor), list_employees_happiness))
print(factor_list_employees_happiness)
average_happiness = sum(factor_list_employees_happiness) / len(list_employees_happiness)
print(average_happiness)
happy_employees = list(filter(lambda x: x >= average_happiness, factor_list_employees_happiness))
print(happy_employees)
if len(happy_employees) >= len(list_employees_happiness)/2:
    print(f"Score: {len(happy_employees)}/{len(list_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(list_employees_happiness)}. Employees are not happy!")
