numbers = input().split(", ")

numbers_without_reverse = ""
numbers_with_reverse = ""

for num in numbers:
    numbers_without_reverse = num
    numbers_with_reverse = num[::-1]
    if numbers_without_reverse == numbers_with_reverse:
        print("True")
    else:
        print("False")
