company_users = {}

command = input()

while command != "End":

    something = command.split(" -> ")

    company_name = something[0]
    employees_id = something[1]

    if company_name not in company_users:
        company_users[company_name] = []

    if employees_id not in company_users[company_name]:
        company_users[company_name].append(employees_id)

    command = input()

for company_name, user_id in company_users.items():

    print(company_name)

    for el in company_users[company_name]:
        print(f"-- {el}")