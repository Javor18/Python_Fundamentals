sequence = list(map(int, input().split(" ")))
counter = 0

while True:
    command = input()

    if command == "End":
        break
    else:
        index = int(command)

        if index < len(sequence) and sequence[index] > -1:
            target = sequence[index]
            sequence[index] = -1

            for i,num in (enumerate(sequence)):

                if num == -1:
                    continue

                if target < num:
                    sequence[i] -= target

                elif target >= num and num > -1:
                    sequence[i] += target

            counter += 1

print(f"Shot targets: {counter} ->", end=" ")
print(" ".join(map(str, sequence)))