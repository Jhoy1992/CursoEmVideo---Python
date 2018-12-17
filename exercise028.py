# Game numbers
import random

randomNumb = random.randint(0,5)
userNumb = int(input('Type a number between 0 and 5: '))

if randomNumb == userNumb:
    print('Congratulations, you win!')
else:  
    print('Sorry, you lose.')