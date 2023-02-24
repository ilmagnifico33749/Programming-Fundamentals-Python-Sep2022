
class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = int(id)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.salary = int(salary)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        annual_salary = 12 * self.salary
        return annual_salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


# ############################################################
# Test_Code_1:
employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
# -----------------------------------------------------------
# Output_1:
# John Smith
# 1500
# 18000
# ############################################################
