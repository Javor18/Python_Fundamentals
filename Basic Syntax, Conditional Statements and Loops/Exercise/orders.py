number_of_orders = int(input())
total_sum = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    need_of_capsules = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if need_of_capsules < 1 or need_of_capsules > 2000:
        continue

    sum = price_per_capsule * need_of_capsules * days
    total_sum += sum

    print(f"The price for the coffee is: ${sum:.2f}")
print(f"Total: ${total_sum:.2f}")