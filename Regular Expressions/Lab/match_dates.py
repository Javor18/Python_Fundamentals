import re

dates = input()

valide_dates = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'

result = re.findall(valide_dates, dates)

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")