words = input().split(" ")
searched_palindrome = input()
palindromes = []
palindrome_count = 0
for word in words:
    if word == word[::-1]:
        palindromes.append(word)



print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")