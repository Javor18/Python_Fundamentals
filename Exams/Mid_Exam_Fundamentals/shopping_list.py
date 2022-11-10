shopping_list = input().split("!")


while shopping_list:

    command = input()
    string_of_command = command.split()

    if command == "Go Shopping!":
        break

    else:
        necessary = string_of_command[0]
        product = string_of_command[1]

    if necessary == "Urgent" and product not in shopping_list:
        shopping_list.insert(0, product)

    elif necessary == "Unnecessary":
        if product in shopping_list:
            shopping_list.remove(product)

    elif necessary == "Correct":

        product_one = string_of_command[1]
        product_two = string_of_command[2]
        if product in shopping_list:
            shopping_list = list(map(lambda x: x.replace(product_one,product_two),shopping_list))

    elif necessary == "Rearrange":
        if product in shopping_list:
            shopping_list.remove(product)
            shopping_list.append(product)

print(", ".join(shopping_list))