import math


def validation(password):
    is_valid = True

    if len(password) < 6 or len(password) > 10:
        is_valid = False
        print(f"Password must be between 6 and 10 characters")

    if not password.isalnum(): #isalnum проверява дали всички подадени стойности са букви или числа
        is_valid = False
        print(f"Password must consist only of letters and digits")

    digits_counter = 0

    for element in password:
        if element.isdigit(): #isdigit проверява дали подадената команда се състои от числа и колко са
            digits_counter += 1

    if digits_counter < 2:
        is_valid = False
        print(f"Password must have at least 2 digits")

    return is_valid

some_password = input()

password_is_valid = validation(some_password)

if password_is_valid:
    print("Password is valid")