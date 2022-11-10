command = input()

while command != "Welcome!":

    name_char = len(command)
    if command == "Welcome!":
        break
    if command == "Voldemort":
        break
    if name_char < 5:
        print(f"{command} goes to Gryffindor.")
    elif name_char == 5:
        print(f"{command} goes to Slytherin.")
    elif name_char == 6:
        print(f"{command} goes to Ravenclaw.")
    elif name_char > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if command == "Voldemort":
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")