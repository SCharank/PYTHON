import random
import Art

print(Art.GuessTheNumber)
a = int(random.choice(range(1,101)))
p = input("Enter the level of difficulty :(easy or hard)(default = hard)")
if p == 'easy':
    Attempts = 10
else:
    Attempts = 5
Guess = False
while not Guess:
    b = int(input("Guess a Number:"))
    if b == a:
        print("Correct Guess!")
        Guess = True
    elif b > a:
        print("Too High!")
        Attempts -= 1
        print(f"Now, you have {Attempts} no of Attempts.")
    else:
        print("Too Low!")
        Attempts -= 1
        print(f"Now, you have {Attempts} no of Attempts.")