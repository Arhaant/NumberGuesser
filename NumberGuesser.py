
import random

number = random.randint(1,10)

chances = 5

while chances>0:
    guess = int(input('Enter your guess: '))
    if guess == number:
        print('Congrats! you got it correct!')
        break
    else:
        print('Your guess was incorrect, try again')
    chances = chances-1

if chances == 0:
    print('Sorry, you ran out of chances')