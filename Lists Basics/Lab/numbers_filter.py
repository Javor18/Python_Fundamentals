number = int(input())

command_even = "even"
command_odd = "odd"
command_negative = "negative"
command_positive = "positive"

numbers = []
filtered_number = []
for i in range (number):
    integer = int(input())
    numbers.append(integer)

command = input()

for integer in numbers:
    filter_command = (
            command == command_even and integer % 2 == 0 or
            command == command_odd and integer % 2 != 0 or
            command == command_positive and integer >= 0 or
            command == command_negative and integer < 0
    )

    if filter_command:
        filtered_number.append(integer)

print(filtered_number)