list_of_numbers_as_str = input().split(" ")
number = int(input())
list_of_numbers_as_digits = []
biggest_digits_as_str = []

for element in list_of_numbers_as_str:
    list_of_numbers_as_digits.append(int(element))

for _ in range(number):
    list_of_numbers_as_digits.remove(min(list_of_numbers_as_digits))


for num in list_of_numbers_as_digits:
    biggest_digits_as_str.append(str(num))

print(', '.join(biggest_digits_as_str))