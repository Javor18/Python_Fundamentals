first_string = input().split(", ")
second_string = input().split(", ")

substrings = []

for first_word in first_string:
    for second_word in second_string:
        if first_word in second_word and not first_word in substrings:
            substrings.append(first_word)

print(substrings)
