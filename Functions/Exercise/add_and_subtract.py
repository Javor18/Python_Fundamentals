
def sum_nums(first,second):
    return first + second

def subtract(sum,third):
    return sum - third

def add_and_subtract(first,second,third):
    sum_add_and_subtract = sum_nums(first,second)
    result = subtract(sum_add_and_subtract,third)
    return result

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num,second_num,third_num))