secret_message = input().split()
final_message = []

for letter in secret_message:
    new_letter = ""
    number = ""
    for character in letter:
        if character.isdigit():
            number += character
        else:
            break
    letter = letter.replace(number, "")
    number = int(number)
    new_letter += chr(number)

    if len(letter) >= 2:
        letter = letter[-1] + letter[1:-1] + letter[0]
    new_letter += letter
    final_message.append(new_letter)

print(" ".join(final_message))