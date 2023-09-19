import random
import Art
import Data

print(Art.HigherLower)
result = True
count = 0
while result:
    a = random.choice(Data.HighrLowerdata)
    b = random.choice(Data.HighrLowerdata)
    print("Compare the below two people:")
    print(f"A : {a['name']},He/She is {a['description']} , He/She is from{a['country']}")
    print(Art.vs)
    print(f"B : {b['name']},He/She is {b['description']} , He/She is from{b['country']}")
    Guess = input("Enter who has more followers:(A or B)").upper()
    if a['follower_count'] > b['follower_count']:
        if Guess == 'B':
            print("Wrong Guess!")
            print(f"Your current score is :{count}")
            result = False
        elif Guess == 'A':
            print("Right Guess!")
            count += 1
            print(f"Your current score is :{count}")
        else:
            print("Invalid Input")
            result = False
    else:
        if Guess == 'A':
            print("Wrong Guess!")
            print(f"Your current score is :{count}")
            result = False
        elif Guess == 'B':
            print("Right Guess!")
            count += 1
            print(f"Your current score is :{count}")
        else:
            print("Invalid Input")
            result = False
