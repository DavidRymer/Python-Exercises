def blackjack(card1, card2):
    if card1 and card2 <= 21:
        return max(card1, card2)
    elif card2 <= 21 < card1:
        return card2
    elif card1 <= 21 < card2:
        return card1
    else:
        return 0


print(blackjack(18, 21))
print(blackjack(21, 18))
print(blackjack(22, 22))



