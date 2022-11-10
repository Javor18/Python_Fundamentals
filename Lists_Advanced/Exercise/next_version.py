version = list(map(int, input().split(".")))

n3 = version[2]
n2 = version[1]
n1 = version[0]

third_num = n3 + 1

if third_num > 9:
    n2 += 1
    third_num = 0

if n2 > 9:
    n1 += 1
    n2 = 0

print(f"{n1}.{n2}.{third_num}")