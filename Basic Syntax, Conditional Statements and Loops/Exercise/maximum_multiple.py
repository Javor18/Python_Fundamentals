divisor = int(input())
boundary = int(input())
max = 0

for integer in range (boundary,divisor, -1):
    if integer % divisor == 0:
        max = integer
        break
print(max)