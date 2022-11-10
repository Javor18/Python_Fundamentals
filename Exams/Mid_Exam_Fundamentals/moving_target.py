sequence_of_targets = list(map(int, input().split(" ")))

command = input()

while command != "End":
    separated_command = command.split()
    task = separated_command[0]

    index = int(separated_command[1])
    letter = separated_command[1]

    power = int(separated_command[2])

    if task == "Shoot":
        if letter in command:
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:
                number = sequence_of_targets[index]
                sequence_of_targets.remove(number)

    if task == "Add":
        if index <= len(sequence_of_targets):
            sequence_of_targets.insert(index, power)
        else:
            print("Invalid placement!")

    if task == "Strike":
        if index <= len(sequence_of_targets):
            number = sequence_of_targets[index]

            last_num  = sequence_of_targets[index - 1]
            new_num = sequence_of_targets[index + 1]

            last_index = index - 1
            new_index = index + 1

            if  index == 0 or last_index < 0 or new_index < 0:
                print("Strike missed!")
                break

            sequence_of_targets.remove(number)

            if last_num in sequence_of_targets:
                sequence_of_targets.remove(last_num)

            if new_num in sequence_of_targets:
                sequence_of_targets.remove(new_num)


    command = input()

str =  list(map(str,sequence_of_targets))

print("|".join(str))
