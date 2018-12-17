# Game numbers
from random import randint
from time import sleep

randomNumb = randint(0,5)
userNumb = int(input('Type a number between 0 and 5: '))

print('Processing...')
sleep(2)

if randomNumb == userNumb:
    print('Congratulations, you win!')
else:  
    print('Sorry, you lose.')