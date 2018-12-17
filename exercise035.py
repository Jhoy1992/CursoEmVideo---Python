straight1 = float(input('Type a length: '))
straight2 = float(input('Type a length: '))
straight3 = float(input('Type a length: '))

straights = [straight1, straight2, straight3]
straights.sort()

if straights[2] < (straights[1] + straights[0]):
    print('This can be a triangle!')
else:
    print('This cannot be a triangle!')
