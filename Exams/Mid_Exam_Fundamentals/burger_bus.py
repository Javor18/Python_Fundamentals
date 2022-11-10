number_of_cities = int(input())
earn_from_tour = 0

for city in range (1, number_of_cities + 1):
    name_of_the_city = input()
    earned_money = float(input())
    expenses = float(input())

    if city % 3 == 0:
        celebrate_expenses = expenses * 0.5
        expenses += celebrate_expenses

    if city % 5 == 0:
        loses = earned_money * 0.10
        earned_money -= loses

    earn_from_city = earned_money - expenses
    earn_from_tour += earn_from_city

    print(f"In {name_of_the_city} Burger Bus earned {earn_from_city:.2f} leva.")
print(f"Burger Bus total profit: {earn_from_tour:.2f} leva.")