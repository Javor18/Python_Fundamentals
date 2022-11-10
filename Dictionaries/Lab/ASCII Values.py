list_of_characters = input().split(", ")
dict = {}
for i in range (len(list_of_characters)):

    key = list_of_characters[i]
    value = ord(key)

    dict[key] = int(value)

print(dict)