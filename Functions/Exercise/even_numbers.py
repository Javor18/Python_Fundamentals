# numbers_as_str = input().split()
#
# numbers_as_digits = []
# 
# for num in numbers_as_str:
#     numbers_as_digits.append(int(num))
#
# even_num = lambda x: x % 2 == 0
#
# result = list(filter(even_num,numbers_as_digits))
#
# print(result)


def is_even(number):
    if int(number) % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []
for current_number in numbers:
    if is_even(current_number):
        filtered_numbers.append(int(current_number))
print(filtered_numbers)