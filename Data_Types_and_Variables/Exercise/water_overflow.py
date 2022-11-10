capacity = 255
number_of_charges = int(input())
charged_water = 0

for charges in range(number_of_charges):
    liters_of_water = int(input())
    charged_water += liters_of_water

    if charged_water > capacity:
        charged_water -= liters_of_water
        print(f"Insufficient capacity!")
print(charged_water)