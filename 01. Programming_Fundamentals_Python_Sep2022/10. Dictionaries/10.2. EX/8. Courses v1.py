my_dict_courses = {}

command = input()
while command != "end":
    command_details = command.split(" : ")
    course_name = command_details[0]
    student_name = command_details[1]

    if course_name not in my_dict_courses.keys():
        my_dict_courses[course_name] = {}
        my_dict_courses[course_name]["students"] = {}
        my_dict_courses[course_name]["students"] = student_name
        my_dict_courses[course_name]["students_count"] = 1
    else:
        my_dict_courses[course_name]["students"] += f', {student_name}'
        my_dict_courses[course_name]["students_count"] += 1

    command = input()

else:
    for course in my_dict_courses.keys():
        print(f"{course}: {my_dict_courses[course]['students_count']}")
        list_students = my_dict_courses[course]["students"].split(", ")
        for student in list_students:
            print(f"-- {student}")

#---------------------------------------------#
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end
#---------------------------------------------#
# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end
#---------------------------------------------#
