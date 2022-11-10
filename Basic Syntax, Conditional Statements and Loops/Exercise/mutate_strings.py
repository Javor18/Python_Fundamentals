first_string = input()
second_string = input()
last_part = first_string

for symbol in range(len(second_string)):
    left_part = second_string[:symbol + 1]
    right_part = first_string[symbol + 1:]
    new_word = left_part + right_part
    if new_word == last_part:
        continue
    print(new_word)
    last_part = new_word