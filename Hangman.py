import random
import Art
import Data

print('You are playing :')
print(Art.Hangman)
print("Let's Start!")

print(f'WELCOME!\nYou are playing:\n{Art.Hangman}')
Word = (random.choice(Data.Hangman_word_list))
Word_len = len(Word)
lives = 7
print(f"You have {lives} attempts to guess the below word.\nIt has {Word_len} letters.\n{Art.Hangman_stages[7]}")
Guessed_letters = ''
while lives > 0:
    # counts user is wrong how many times
    failed = 0
    for char in Word:
        if char in Guessed_letters:
            print(char, end='')
        else:
            print('_', end='')
            failed += 1
    if failed == 0:
        print(f'YOU WIN!\nThe word was {Word}')
        break
    guess = input('\nEnter a charecter to check:').lower()
    Guessed_letters += guess
    if guess not in Word:
        print(f'{Art.Hangman_stages[lives - 1]}\nWrong charecter.\nYou now have only {lives -1} attempts.')
        lives -= 1
if lives == 0:
    print(f'YOU LOSE!.\nThe word was {Word}')