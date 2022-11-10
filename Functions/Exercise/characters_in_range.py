first_character = input()
second_character = input()

def ascii_characters(first_character,second_character):
    collected_characters = []
    for character in range(ord(first_character) + 1,ord(second_character)):
        collected_characters.append(chr(character))
    return collected_characters


result = ascii_characters(first_character,second_character)

print(' '.join(result))