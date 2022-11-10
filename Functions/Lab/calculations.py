
def solve(a, b, operator):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b

operation = input()
first_number = int(input())
second_number = int(input())

print(solve(first_number, second_number, operation))

# import operator
#
# def calculations(num_a, num_b, operation):
#     operations_dict = {'multiply': operator.mul, 'divide': operator.truediv, 'add': operator.add, 'subtract': operator.sub}
#     return (operations_dict[operator](num_a,num_b))
#
# type_of_operation = input()
# first_num = int(input())
# second_num = int(input())
#
# print(calculations(first_num, second_num, type_of_operation))