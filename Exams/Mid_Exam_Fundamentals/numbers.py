numbers = list(map(int, input().split(" ")))


while numbers:
    command = input()
    if command == "Finish":
        break
    else:
        string_of_command = command.split()
        task = string_of_command[0]
        value = int(string_of_command[1])

    if task == "Add":
        numbers.append(value)

    if task == "Remove":
        if value in numbers:
            numbers -= value

    if task == "Replace":
        replacement = string_of_command[2]
        if value in numbers:
            numbers = list(map(lambda x: x.replace(value,replacement,1),numbers))

    if task == "Collapse":
        for num in numbers:
            if num < value:
                numbers.remove(num)

    command = input().split()

print(numbers)