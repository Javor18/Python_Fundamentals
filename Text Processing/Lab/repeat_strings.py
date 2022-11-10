strings = input().split(" ")
total_word = ''

for word in strings:

    length = len(word)
    total_word += word * length
print(total_word)