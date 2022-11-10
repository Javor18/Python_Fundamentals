number = int(input())
given_word = input()

without_the_given_word_list = []
including_the_given_word_list = []

for i in range (number):
    word = input()
    without_the_given_word_list.append(word)

    if given_word in word:
        including_the_given_word_list.append(word)

print(without_the_given_word_list)
print(including_the_given_word_list)