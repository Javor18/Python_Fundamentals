students_count = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())

max_attendance_per_student = []
max_bonus_points_per_student = []

for student in range (1, students_count + 1):
    attendance_per_student = int(input())
    max_attendance_per_student.append(attendance_per_student)
    bonus_points_per_student = (attendance_per_student / total_number_of_lectures) * (5 + additional_bonus)
    max_bonus_points_per_student.append(bonus_points_per_student)

print(f"Max Bonus: {max(max_bonus_points_per_student):.0f}.")
print(f"The student has attended {max(max_attendance_per_student)} lectures.")