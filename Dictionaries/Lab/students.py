inp = []
while True:
    data = input().split(":")
    if len(data) == 1:
        break
    inp.append(data)

students_dict = {course[2].replace(" ", "_"): {} for course in inp}
for course in inp:
    students_dict[course[2].replace(" ", "_")][course[0]] = int(course[1])

out = [f"{user} - {students_dict[data[0]][user]}" for user in students_dict[data[0]]]
print(*out, sep="\n")