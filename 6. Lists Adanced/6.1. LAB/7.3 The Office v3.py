orig_employees_happiness = list(map(int, input().split(" ")))
happiness_factor = int(input())
final_employees_happiness = list(map(lambda x: x * happiness_factor, orig_employees_happiness))
medium_happiness = sum(final_employees_happiness) / len(final_employees_happiness)
filtered_list = list(filter(lambda x: x >= medium_happiness, final_employees_happiness))
def happiness_thing(list_one, list_two):
    def list_all_employees(list_one, list_two):
        total_employees = len(list_one)
        happy_employees = len(list_two)
        unhappy_employees = len(list_one) - len(list_two)
        list_employees = [total_employees, happy_employees, unhappy_employees]
        return list_employees
    def happiness_score(list):
        return f"Score: {list[1]}/{list[0]}."
    def happines_state(list):
        happiness = False
        if list[1] >= list[2]:
            happiness == True
            return f"Employees are happy!"
        else:
            return f"Employees are not happy!"
    return f"{happiness_score(list_all_employees(list_one,list_two))} {happines_state(list_all_employees(list_one, list_two))}"
print(happiness_thing(final_employees_happiness, filtered_list))


