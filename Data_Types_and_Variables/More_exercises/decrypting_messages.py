key = int(input())
number_of_lines = int(input())
key_two = ""
for _ in range(number_of_lines):
    letter = input()
    key_one = ord(letter) + key
    key_two += chr(key_one)

print(key_two)