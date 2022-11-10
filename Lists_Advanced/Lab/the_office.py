employee_happiness = input().split(" ")
happiness_factor = int(input())

employee_happiness = list(map(lambda x : int(x) * happiness_factor, employee_happiness))
filtered_employees = list(filter(lambda x : x >= (sum(employee_happiness) / len(employee_happiness)), employee_happiness))

if len(filtered_employees) >= len(employee_happiness) / 2:
    print(f"Score: {len(filtered_employees)}/{len(employee_happiness)}. Employees are happy!")

else:
    print(f"Score: {len(filtered_employees)}/{len(employee_happiness)}. Employees are not happy!")