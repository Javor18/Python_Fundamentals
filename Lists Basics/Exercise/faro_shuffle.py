deck_of_card = input().split()
count_of_shuffles = int(input())

for shuffle in range (count_of_shuffles):
    final_deck = []
    mid_of_deck = len(deck_of_card) // 2
    left_part = deck_of_card[0:mid_of_deck]
    right_part = deck_of_card[mid_of_deck:]
    for card in range (len(left_part)):
        final_deck.append(left_part[card])
        final_deck.append(right_part[card])
    deck_of_card = final_deck
print(deck_of_card)