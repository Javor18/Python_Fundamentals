import re

phone_numbers = input()

valid_phone_numbers = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

result = re.findall(valid_phone_numbers, phone_numbers)

print(', '.join(result))