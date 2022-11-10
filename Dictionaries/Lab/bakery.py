products = input().split(' ')

# bakery = {}
#
# for i in range (0, len(products), 2):
#     key = products[i]
#     value = products[i + 1]
#     bakery[key] = int(value)
#
# print(bakery)

products_dict = {products[i]: int(products[i + 1]) for i in range(0, len(products), 2)}

print(products_dict)