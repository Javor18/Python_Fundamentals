
neighborhood = list(map(int,input().split("@")))

command = input()
jump_length = 0
while command != 'Love!':
    string_for_house_and_jump = command.split()
    jump_power = int(string_for_house_and_jump[1])
    jump_length += jump_power

    if len(neighborhood) > jump_length:
        if neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
    else:
        jump_length = 0
        if neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighborhood[jump_length] -= 2
            if neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
    command = input()

counter = 0
for n in neighborhood:
    if n > 0:
        counter += 1

print(f"Cupid's last position was {jump_length}.")
if  counter != 0:
    print(f"Cupid has failed {counter} places.")
else:
    print("Mission was successful.")

