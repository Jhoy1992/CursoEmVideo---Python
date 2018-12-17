num1 = int(input('Type a number: '))
num2 = int(input('Type a number: '))
num3 = int(input('Type a number: '))

if num1 > num2 and num1 > num3:
    print('The biggest number is: {}'.format(num1))
if num2 > num1 and num2 > num3:
    print('The biggest number is: {}'.format(num2))
if num3 > num2 and num3 > num1:
    print('The biggest number is: {}'.format(num3))

if num1 < num2 and num1 < num3:
    print('The smallest number is: {}'.format(num1))
if num2 < num1 and num2 < num3:
    print('The smallest number is: {}'.format(num2))
if num3 < num2 and num3 < num1:
    print('The smallest number is: {}'.format(num3))