carSpeed = int(input('Type the car speed: '))

if carSpeed > 80:
    print('You have been fined!')
    print('Your traffic ticket will cost ${}.'.format((carSpeed - 80) * 7)) 
