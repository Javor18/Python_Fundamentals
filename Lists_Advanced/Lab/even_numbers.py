number_list = list(map(int,input().split(", ")))

index = [i for i in range(len(number_list)) if number_list[i] % 2 == 0]

print(index)