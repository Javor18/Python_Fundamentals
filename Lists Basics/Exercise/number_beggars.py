sums_list_as_strings = input().split(", ")
count_of_beggars = int(input())
sums_list_as_digits = []
counter_of_index = 0
final_list = []

for element in sums_list_as_strings:
    sums_list_as_digits.append(int(element))
while counter_of_index < count_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(counter_of_index,len(sums_list_as_digits),count_of_beggars):
        sum_of_current_beggar += sums_list_as_digits[current_index]
    counter_of_index += 1
    final_list.append(sum_of_current_beggar)
print(final_list)