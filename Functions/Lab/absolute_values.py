
numbers = input().split()

numbers_as_float = []

for num in numbers:

    numbers_as_float.append(abs(float(num)))

print(numbers_as_float)