command = input()
product_quantity = {}
product_price = {}

while command != "buy":
    something = command.split()

    product_name = something[0]
    price = float(something[1])
    quantity = int(something[2])

    if product_name not in product_quantity.keys():
        product_quantity[product_name] = 0
        product_price[product_name] = 0.00
    product_quantity[product_name] += quantity
    product_price[product_name] = price

    command = input()

for product_name, quantity in product_quantity.items():
    total_price = quantity * product_price[product_name]

    print(f"{product_name} -> {total_price:.2f}")