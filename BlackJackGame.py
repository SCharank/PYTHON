#Rules:
'''
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
'''
import Art
import random
print(Art.BlackJack)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Card_draw = False
a = random.choice(cards)
b = random.choice(cards)
c = random.choice(cards)
d = random.choice(cards)
print(f"Your cards are: {a} and {b}")
print(f"And\nYour Dealer's cards are : {c} and Unknown")
while not Card_draw:
    if a + b == 21:
        print("You Win!")
        Card_draw = True
        break
    elif c + d == 21:
        print("You Loose")
        Card_draw = True
        break
    elif a + b > 21:
        if (a == 11 | b == 11):
            if a + b - 10 > 21:
                print("You Lose")
                Card_draw = True
                break
    else:
        f = input("Do you want to take another card:")
        q = random.choice(cards)
        if f =='n':
            if c + d < 17:
                c += q
                continue
            else:
                if c + d > a + b:
                    print("You Loose!")
                    Card_draw = True
                    break
                else:
                    print("You Win!")
                    Card_draw = True
                    break
        else:
            print(f"Your next card is: {q}")
            a += q
            continue