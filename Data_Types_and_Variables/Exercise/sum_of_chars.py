n = int(input())
total_sum = 0

for _ in range(n):
    number = input()
    total_sum += ord(number)

print(f"The sum equals: {total_sum}")

