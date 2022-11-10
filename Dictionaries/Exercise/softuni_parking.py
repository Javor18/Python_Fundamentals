parking_lot = {}

count_of_cars = int(input())

for i in range (count_of_cars):

    command = input().split()

    task = command[0]
    username = command[1]

    if task == "register":
        license_plate_number = command[2]

        if username not in parking_lot or parking_lot[username] == 0:
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

        else:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")

    else:

        if username not in parking_lot:
            print(f"ERROR: user {username} not found")

        else:
            parking_lot[username] = 0
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking_lot.items():
    if parking_lot[username] != 0:
        print(f"{username} => {license_plate_number}")
