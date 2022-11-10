numbers = list(map(int,input().split()))

command = input().split()

while command != 'end':
    task = command[0]
    if task == 'end':
        break

    if task == 'swap':
        numbers[int(command[1])] , numbers[int(command[2])] = numbers[int(command[2])], numbers[int(command[1])]

    elif task == 'multiply':
        numbers[int(command[1])] *= numbers[int(command[2])]

    if task == 'decrease':
        numbers = [x - 1 for x in numbers]

    command = input().split()

string_of_el = list(map(str, numbers))

print(', '.join(string_of_el))