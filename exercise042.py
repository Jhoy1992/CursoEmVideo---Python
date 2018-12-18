straight1 = float(input('Type a length: '))
straight2 = float(input('Type a length: '))
straight3 = float(input('Type a length: '))

straights = [straight1, straight2, straight3]
straights.sort()

if straights[2] < (straights[1] + straights[0]):
    if straights[0] == straights[1] == straights[2]:
        print('This can be a triangle "EQUILÁTERO"!')
    elif straights[0] == straights[1] or straights[0] == straights[2] or straights[2] == straights[1]:
        print('This can be a triangle "ISÓSCELES"!')
    else:
        print('This can be a triangle "ESCALENO"!')
else:
    print('This cannot be a triangle!')