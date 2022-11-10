command = input()
coffee = 0
total_coffee = 0
while command != "END":

    if command == "coding":
        coffee += 1
    elif command == "CODING":
        coffee += 2
    elif command == "dog" or command == "cat":
        coffee += 1
    elif command == "DOG" or command == "CAT":
        coffee += 2
    elif command == "movie":
        coffee += 1
    elif command == "MOVIE":
        coffee += 2

    command = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)