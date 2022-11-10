
def smallest_num(some_nums):
    return min(some_nums)


first_num = int(input())
second_num = int(input())
third_num = int(input())

all_num = [first_num, second_num , third_num]

min_num = smallest_num(all_num)

print(min_num)