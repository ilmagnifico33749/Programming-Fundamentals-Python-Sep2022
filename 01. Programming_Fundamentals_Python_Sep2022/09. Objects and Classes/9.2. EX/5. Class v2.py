class Class:
    students_count = 22

    def __init__(self, name):
        self.name = name
        self.list_students = []
        self.list_grades = []

    def add_student(self, name: str, grade: float):
        self.students_count = 0
        if self.students_count < Class.students_count:
            self.list_students.append(name)
            self.list_grades.append(grade)
            self.students_count += 1

    def get_average_grade(self):
        self.average_grade = (sum(self.list_grades) / len(self.list_grades))
        return f"{self.average_grade:.2f}"
        #OR
        #self.sum_grade = sum(self.list_grades)
        #self.len_grades = len(self.list_grades)
        #self.average_grade = f"{(self.sum_grade / self.len_grades):.2f}"
        #return self.average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.list_students)}.\nAverage grade: {Class.get_average_grade(self)}"

# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)