usernames = input().split(", ")

for username in usernames:
    is_valid = True

    if not 3 <= len(username) <= 16:
        is_valid = False

    for character in username:

        if not (character.isalnum() or character == "_" or character == "-"):
            is_valid = False

    if ' ' in username:
        is_valid = False

    if is_valid:
        print(username)