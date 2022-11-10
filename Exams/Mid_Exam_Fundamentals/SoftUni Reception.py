first_lector = int(input())
second_lector = int(input())
third_lector = int(input())
students_count = int(input())
can_handle = 0
hour = 0

for _ in range(0, students_count + 1):

    can_handle = first_lector + second_lector + third_lector
    if students_count <= 0:
        break

    else:
        students_count -= can_handle
        hour += 1

    if hour % 4 == 0:
        hour += 1

print(f"Time needed: {hour}h.")
