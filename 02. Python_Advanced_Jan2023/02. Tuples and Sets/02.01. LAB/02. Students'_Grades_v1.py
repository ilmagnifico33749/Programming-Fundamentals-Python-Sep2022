students = int(input())
my_dict_students = {}

for student in range(students):
    student, grade = tuple(input().split(" "))
    if student not in my_dict_students:
        my_dict_students[student] = [f"{float(grade):.2f}"]
    else:
        my_dict_students[student].append(f"{float(grade):.2f}")

for key, value in my_dict_students.items():
    average_grades = sum([float(x) for x in my_dict_students[key]])/len(list(my_dict_students[key]))
    print(f"{key} -> {' '.join(value)} (avg: {average_grades:.2f})")

#####################################
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
# -----------------------------------
# Output:
# Mark -> 5.50 2.50 3.46 (avg: 3.82)
# Peter -> 5.20 3.20 (avg: 4.20)
# Alex -> 2.00 3.00 (avg: 2.50)
#####################################
# Input_2:
# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66
# Output_2:
# Ted -> 3.00 3.66 (avg: 3.33)
# Scott -> 4.50 5.00 (avg: 4.75)
#####################################
# Input_3:
# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30
# ------------------------------------
# Output_3:
# Peter -> 4.40 (avg: 4.40)
# Lee -> 6.00 5.50 6.00 (avg: 5.83)
# Kenny -> 3.30 (avg: 3.30)
#####################################
