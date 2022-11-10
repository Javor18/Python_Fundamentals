food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
pig_weight = float(input()) * 1000
total_used_hay = 0
total_used_cover = 0

for day in range(1, 31):
    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        break

    food_for_day = 300 #gr
    food_quantity -= food_for_day

    if day % 2 == 0:
        hay_for_day = food_quantity * 0.05
        hay_quantity -= hay_for_day
        total_used_hay += hay_for_day

    if day % 3 == 0:
        cover_for_the_day = pig_weight / 3
        total_used_cover += cover_for_the_day
        cover_quantity -= cover_for_the_day

if food_quantity > 0 and hay_quantity > 0 and cover_quantity > 0:
    print(f"Everything is fine! Puppy is happy! Food: {(food_quantity / 1000):.2f}, Hay: {(hay_quantity / 1000):.2f},\
 Cover: {(cover_quantity / 1000):.2f}.")

else:
    print("Merry must go to the pet store!")
