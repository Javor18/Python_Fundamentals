import re

names = input()

searched_names = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"

result = re.findall(searched_names, names)

print(" ".join(result))