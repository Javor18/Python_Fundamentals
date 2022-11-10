number_of_electrons = int(input())
shells = []
n = 0
while number_of_electrons > 0:
    n += 1
    shell = 2 * n ** 2

    if number_of_electrons >= shell:     # проверка дали има място за максималния капаците
        shells.append(shell)
        number_of_electrons -= shell

    else:                                            # ако няма попълваме колкото е останало
        shells.append(number_of_electrons)
        number_of_electrons = 0

print(shells)