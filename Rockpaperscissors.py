""" Rock, Paper, Scissors: Computer vs Player """
import random
options = ['rock', 'paper', 'scissors']

def rps():
    computerscore = 0
    playerscore = 0
        
    while True:
        if playerscore == 10:
            print('You win! Game over!')
            break
        elif computerscore == 10:
            print('You lose! Game over!')
            break
        player = input('Choose: Rock, Paper or Scissors: ')
        player = player.lower()
        print('Player: ' + player)
        computer = random.choice(options)
        print('Computer: ' + computer)
        if player == 'rock' and computer == 'scissors':
            print('You win!')
            playerscore = playerscore + 1
            print('Player Score: ')
            print(playerscore)
            print('Computer Score: ')
            print(computerscore)
        elif player == 'scissors' and computer == 'paper':
            print('You win!')
            playerscore = playerscore + 1
            print('Player Score: ')
            print(playerscore)
            print('Computer Score: ')
            print(computerscore)
        elif player == 'paper' and computer == 'rock':
            print('You win!')
            playerscore = playerscore + 1
            print('Player Score: ')
            print(playerscore)
            print('Computer Score: ')
            print(computerscore)
        elif player == 'rock' and computer == 'rock':
            print('Tie!')
        elif player == 'paper' and computer == 'paper':
            print('Tie!')
        elif player == 'scissors' and computer == 'scissors':
            print('Tie!')
        elif player == 'scissors' and computer == 'rock':
            print('You lose!')
            computerscore = computerscore + 1
            print('Player Score: ')
            print(playerscore)
            print('Computer Score: ')
            print(computerscore)
        elif player == 'paper' and computer == 'scissors':
            print('You lose!')
            computerscore = computerscore + 1
            print('Player Score: ')
            print(playerscore)
            print('Computer Score: ')
            print(computerscore)
        elif player == 'rock' and computer == 'paper':
            print('You lose!')
            computerscore = computerscore + 1
            print('Player Score: ')
            print(playerscore)
            print('Computer Score: ')
            print(computerscore)
            
            

rps()
    
