""" Guess the number game """
import random

def guessGame():
    trueNumber = random.randint(1,100)
    while True:
        try:
            userGuess = int(input('Guess a number between 1 and 100: '))
            if userGuess == trueNumber:
                print('You got it!')
                break
            elif userGuess > trueNumber:
                print('Guess Lower.')
            else:
                print('Guess Higher.')
        except ValueError:
            print('Please only use number values.')
            

        
guessGame()


        
