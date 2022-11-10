# x = [1,4,9,1,5,3,2]
#
# result = sorted(x)
#
# print(result)

numbers = input().split()

number_as_digits = []

for num in numbers:
    number_as_digits.append(int(num))

result = sorted(number_as_digits)

print(result)