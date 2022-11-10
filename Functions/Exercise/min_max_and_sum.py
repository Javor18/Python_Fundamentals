numbers_as_str = input().split()

numbers_as_digits = []

for num in numbers_as_str:
    numbers_as_digits.append(int(num))

print(f"The minimum number is {min(numbers_as_digits)}")
print(f"The maximum number is {max(numbers_as_digits)}")
print(f"The sum number is: {sum(numbers_as_digits)}")