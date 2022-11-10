initial_energy = 100
initial_coins = 100

list_of_events = input().split("|")
bakery_is_open = True

for event in list_of_events:
    event_info = event.split("-")
    type_of_event = event_info[0]
    number = int(event_info[1])

    if type_of_event == "rest":
        temporary_energy = initial_energy
        initial_energy += number
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif type_of_event == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            temporary_coins = initial_coins
            initial_coins += number
            earned_coins = initial_coins - temporary_coins
            print(f"You earned {earned_coins} coins.")
        else:
            initial_energy += 50
            if initial_energy > 100:
                initial_energy = 100
            print("You had to rest!")
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            bakery_is_open = False
            break

if bakery_is_open == True:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")