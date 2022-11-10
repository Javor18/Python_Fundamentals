def odd_or_even(number : int):
    odd_sum = 0
    even_sum = 0
    number_as_str = str(number)
    for element in number_as_str:
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

digit = int(input())

print(odd_or_even(digit))