century = int(input())
year = century * 100
days = int(365.2422  * year)
hours = days * 24
minutes = hours * 60

print(f"{century} centuries = {year} years = {days} days = {hours} hours = {minutes} minutes")