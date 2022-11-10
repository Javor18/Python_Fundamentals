quantity = int(input())
days = int(input())
price = 0
christmas_spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        price += ornament_set * quantity
        christmas_spirit += 5

    if day % 3 == 0:
        price += (tree_skirt + tree_garland) * quantity
        christmas_spirit += 13

    if day % 5 == 0:
        price += tree_lights * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        price += tree_skirt + tree_garland + tree_lights

if days % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {price}")
print(f"Total spirit: {christmas_spirit}")