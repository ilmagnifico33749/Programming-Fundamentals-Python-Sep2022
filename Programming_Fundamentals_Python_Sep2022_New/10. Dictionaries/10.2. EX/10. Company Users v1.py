my_dict_companies_employees = {}

command = input()
while command != "End":
    command_details = command.split(" -> ")
    company_name = command_details[0]
    employee_id = command_details[1]

    if company_name not in my_dict_companies_employees.keys():
        my_dict_companies_employees[company_name] = {}
        my_dict_companies_employees[company_name] = employee_id
    else:
        if employee_id in my_dict_companies_employees[company_name]:
            pass
        else:
            my_dict_companies_employees[company_name] += ', ' + employee_id

    command = input()

else:
    for company in my_dict_companies_employees.keys():
        print(company)
        list_employees = (my_dict_companies_employees[company]).split(", ")
        for employee in list_employees:
            print(f"-- {employee}")

# ----------------------#
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
# ----------------------#
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End
# ----------------------#
