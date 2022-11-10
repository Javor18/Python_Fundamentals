def check_chairs(number_of_rooms):
    total_free_chairs = 0
    needed_chair = 0

    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs,visitors = input().split()
        left_chairs = len(free_chairs) - int(visitors)

        if left_chairs >= 0:
            total_free_chairs += left_chairs

        else:
            needed_chair += abs(left_chairs)
            print(f"{abs(left_chairs)} more chairs needed in room {number_of_room}")
    return total_free_chairs, needed_chair

number_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(number_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")