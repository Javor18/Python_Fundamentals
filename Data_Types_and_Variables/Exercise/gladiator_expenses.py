lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
shield_counter = 0

for lost_game in range(1, lost_fights + 1):

    if lost_game % 2 == 0 and lost_game % 3 == 0:
        broken_helmet += 1
        broken_sword += 1
        broken_shield += 1
        shield_counter +=1

    elif lost_game % 2 == 0:
        broken_helmet += 1

    elif lost_game % 3 == 0:
        broken_sword += 1

    if shield_counter % 2 == 0 and shield_counter != 0:
        broken_armor += 1
        shield_counter = 0

helmet_repair_price = broken_helmet * helmet_price
sword_repair_price = broken_sword * sword_price
shield_repair_price = broken_shield * shield_price
armor_repair_price = broken_armor * armor_price

total_expenses = helmet_repair_price + sword_repair_price + shield_repair_price + armor_repair_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")