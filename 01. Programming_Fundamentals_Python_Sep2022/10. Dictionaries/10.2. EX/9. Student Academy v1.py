my_dict_students = {}

number_of_commands = int(input())
for times in range(number_of_commands):
    student_name = str(input())
    student_grade = f"{float(input()):.2f}"
    if student_name not in my_dict_students.keys():
        my_dict_students[student_name] = {}
        my_dict_students[student_name] = student_grade
    else:
        my_dict_students[student_name] += f", {student_grade}"

for student in my_dict_students.keys():
    sum_all_grades = sum(list(map(float, (my_dict_students[student]).split(", "))))
    number_of_grades = len(list(my_dict_students[student].split(', ')))
    average_grade = sum_all_grades / number_of_grades
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")

#----------#
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5
#----------#
# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6
#----------#
