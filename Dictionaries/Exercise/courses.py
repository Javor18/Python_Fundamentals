course_list = {}

command = input()

while command != "end":
    course_name, student_name = command.split(" : ")

    if course_name not in course_list:
        course_list[course_name] = []
        course_list[course_name].append(student_name)
    else:
        course_list[course_name].append(student_name)

    command = input()

for course_name, registered_students in course_list.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")