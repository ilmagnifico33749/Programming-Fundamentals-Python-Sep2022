orig_employees_happiness = list(map(int, input().split(" ")))
happiness_factor = int(input())
final_employees_happiness = list(map(lambda x: x * happiness_factor, orig_employees_happiness))
medium_happiness = sum(final_employees_happiness) / len(final_employees_happiness)
verifying_list = list(map(lambda x: x if x >= medium_happiness else "NOT", final_employees_happiness))
count_happy_employees = len(final_employees_happiness) - verifying_list.count("NOT")
if count_happy_employees >= (len(final_employees_happiness) / 2):
    print(f"Score: {count_happy_employees}/{len(final_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {count_happy_employees}/{len(final_employees_happiness)}. Employees are not happy!")
