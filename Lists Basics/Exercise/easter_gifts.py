# gifts = input().split(' ')
# command = input()
#
# while command != "No Money":
#     command = input().split(" ")
#     availability = command[0]
#     gift = command[1]
#
#     if availability == "OutOfStock":
#         for i in range (len(gifts)):
#             if gift in gifts[i]:
#                 gift[i] = 'None'
#
#     elif availability == "Required":
#         for i in range(len(gifts)):
#             if i == int(command[2]):
#                 gifts[i] = command[1]
#
#     elif availability == "JustInCase":
#         gifts[-1] = gift
# command = input()
#
# while "None" in gifts:
#     gifts.remove("None")
#
# print(''.join(gifts))


name_of_the_gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    to_do_command = command[0]
    gift = command[1]
    if to_do_command == 'OutOfStock':
        for index in range(len(name_of_the_gifts)):
            if gift in name_of_the_gifts[index]:
                name_of_the_gifts[index] = 'None'

    elif to_do_command == 'Required':
        for index in range(len(name_of_the_gifts)):
            if index == int(command[2]):
                name_of_the_gifts[index] = command[1]

    elif to_do_command == 'JustInCase':
        name_of_the_gifts[-1] = gift
    command = input()

while 'None' in name_of_the_gifts:
    name_of_the_gifts.remove('None')

print(' '.join(name_of_the_gifts))