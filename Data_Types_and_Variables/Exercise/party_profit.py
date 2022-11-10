import math

groups_size = int(input())
days_of_adventure = int(input())
coins = 0

for days in range(1,days_of_adventure + 1):

    if days % 10 == 0:
        groups_size -= 2

    if days % 15 == 0:
        groups_size += 5

    if days % 5 == 0 and days % 3 == 0:
        coins += groups_size * 20
        coins -= groups_size * 5

    elif days % 3 == 0:
        coins -= groups_size * 3

    elif days % 5 == 0:
        coins += groups_size * 20

    coins += 50
    coins -= groups_size * 2

coins_per_member = coins / groups_size
print(f"{groups_size} companions received {math.floor(coins_per_member)} coins each.")
