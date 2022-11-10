shopping_list = input().split(", ")


while shopping_list:
    command = input()

    if command == "Craft!":
        break

    else:
        string = command.split(" - ")

    task = string[0]
    product = string[1]

    if task == "Collect" and product not in shopping_list:
        shopping_list.append(product)

    if task == "Drop" and product in shopping_list:
       shopping_list.remove(product)

    if task == "Combine Items":
        old_and_new = product.split(":")
        old = old_and_new[0]
        new = old_and_new[1]

        if old in shopping_list:
            index_of_old = shopping_list.index(old)
            shopping_list.insert(index_of_old + 1, new)

    if task == "Renew" and product in shopping_list:
        shopping_list.remove(product)
        shopping_list.append(product)

print(", ".join(shopping_list))