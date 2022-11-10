initial_health = 100
initial_bitcoins = 0
live = True
counter = 0

dungeons_rooms = input().split("|")

letter = []
for index in range (0, len(dungeons_rooms) + 1):
    counter += 1
    word = dungeons_rooms[index]


    str = word.split()

    command = str[0]
    number = int(str[1])

    if command == "potion":

        initial_health += number

        if initial_health > 100:
            healing = initial_health - number
            heal = 100 - healing
            initial_health = 100
            print(f"You healed for {heal} hp.")

        else:
            print(f"You healed for {number} hp.")

        print(f"Current health: {initial_health} hp.")

    if command == "chest":

        initial_bitcoins += number

        if live == True:
            print(f"You found {number} bitcoins.")

    if command != "potion" and command != "chest":
        initial_health -= number

        if initial_health > 0:
            print(f"You slayed {command}.")


        else:
            print(f"You died! Killed by {command}.")
            room = index + 1
            print(f"Best room: {room}")
            live = False

    if counter == len(dungeons_rooms):
        break


if live == True:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
