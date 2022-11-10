student_information = {}
grade_count = {}

count_of_rows = int(input())

for i in range (count_of_rows):

    student_name = input()
    student_grade = float(input())

    if student_name not in student_information:
        student_information[student_name] = 0
        grade_count[student_name] = 0

    if student_name in student_information:
        student_information[student_name] += student_grade
        grade_count[student_name] += 1

for name, average_grade in student_information.items():
    count = grade_count[name]
    total_grade = average_grade / count

    if total_grade >= 4.5:

        if average_grade > 6 and total_grade >= 4.5:
            count = grade_count[name]
            print(f"{name} -> {(total_grade):.2f}")

        else:
            print(f"{name} -> {average_grade:.2f}")