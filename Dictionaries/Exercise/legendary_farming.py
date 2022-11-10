resources = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
command = input().split()

while obtained == False:

    for i in range(0, len(command), 2):
        value = int(command[i])
        key = command[i + 1].lower()

        if key not in resources.keys():
            resources[key] = 0
        resources[key] += value

        if resources["shards"] >= 250:
            print("Shadowmourne obtained!")
            resources["shards"] -= 250
            obtained = True

        elif resources["fragments"] >= 250:
            print("Valanyr obtained!")
            resources["fragments"] -= 250
            obtained = True

        elif resources["motes"] >= 250:
            print("Dragonwrath obtained!")
            resources["motes"] -= 250
            obtained = True

        if obtained:
            break
    if obtained:
        break

    command = input().split()

for material, quantity in resources.items():
    print(f"{material}: {quantity}")
