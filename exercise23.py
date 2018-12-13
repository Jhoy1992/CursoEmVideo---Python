Number = input('Type a number between 0 and 9999: ')

if len(Number) > 0 :
    print('Unidade: {}'.format(Number[:1]))

if len(Number) > 1 :
    print('Dezena: {}'.format(Number[:2:-1]))

if len(Number) > 2 :
    print('Centena: {}'.format(Number[:3]))

if len(Number) > 3 :
    print('Milhar: {}'.format(Number[:4]))