initial_energy = int(input())
won_battles = 0
finished = True

while True:
    command = input()

    if command == "End of battle":
        break
    else:
        distance = int(command)

    if initial_energy >= distance:
        won_battles += 1
        initial_energy -= distance
    else:
        finished = False
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break

    if won_battles % 3 == 0:
        initial_energy += won_battles

if finished == True:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}" )
