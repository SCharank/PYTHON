import random
import Art

print("Welcome to Rock-Paper-Scissors game")
C1 = input("Yor choice ('R' or 'P' or 'S')")
if C1 == 'R':
    print('rock:')
    print(Art.RPF_rock)
elif C1 == 'S':
    print('scissors:')
    print(Art.RPF_scissors)
elif C1 == 'P':
    print('paper:')
    print(Art.RPF_paper)
else:
    print("Invalid Choice.\nGame Over.")
L = ['R', 'S', 'P']
C2 = random.choice(L)
if C2 == 'R':
    print('rock:')
    print(Art.RPF_rock)
    if C1 == 'P':
        print("You Win!")
    elif C1 == 'S':
        print("You Lose!")
    elif C1 == 'R':
        print("Tie!")
elif C2 == 'S':
    print('scissors:')
    print(Art.RPF_scissors)
    if C1 == 'R':
        print("You Win!")
    elif C1 == 'P':
        print("You Lose!")
    elif C1 == 'S':
        print("Tie!")
elif C2 == 'P':
    print('paper:')
    print(Art.RPF_paper)
    if C1 == 'S':
        print("You Win!")
    elif C1 == 'R':
        print("You Lose!")
    elif C1 == 'P':
        print("Tie!")