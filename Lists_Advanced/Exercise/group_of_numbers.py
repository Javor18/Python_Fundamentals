# def biggest_group(max_num: int):
#     biggest_group = (max_num // 10 + 1) * 10
#     if max_num % 10 == 0:
#         biggest_group -= 10
#     return biggest_group
#
#
# numbers_list = list(map(int , input().split(", ")))
# max_num = max(numbers_list)
# biggest_group = biggest_group(max_num)
# number_groups = []
# for _ in range(biggest_group // 10):
#     number_groups.append([])
# for number in numbers_list:
#     index = number // 10
#     if number % 10 == 0 and number != 0:
#         index -= 1
#     number_groups[index].append(number)
# groups_list = [f"Group of {(x + 1) * 10}'s: {number_groups[x]}" for x in range(len(number_groups))]
# print(*groups_list, sep='\n')

numbers = list(map(int, input().split(", ")))
max_group = max(numbers) // 10

last_max = 0
n = 1

while numbers:
    new_max = int(f'{n}0')
    current_range = [num for num in numbers if num in range(last_max, new_max + 1)]
    numbers = [num for num in numbers if num not in current_range]
    print('Group of', f"{n}0's:", current_range)
    last_max = new_max
    n += 1