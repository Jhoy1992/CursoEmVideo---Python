number = int(input('Type a number:'))
convert = int(input('What is the conversion base? (1 - Binary 2 - Octal 3 - Hexdecimal) '))

if convert == 1:
    print('You number {} in binary is {}.'.format(number, bin(number)))
elif convert == 2:
    print('You number {} in binary is {}.'.format(number, oct(number)))
else:
    print('You number {} in binary is {}.'.format(number, hex(number)))