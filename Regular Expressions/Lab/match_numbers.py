import re

numbers = input()

valide_numbers = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

result = re.finditer(valide_numbers, numbers)

for match in result:
    print(match.group(), end=" ")