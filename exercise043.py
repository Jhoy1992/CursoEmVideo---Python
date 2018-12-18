weight = float(input('What is your weight? '))
height = float(input('What is your height? '))

imc = weight / (height * height)

if imc < 18.5:
    print('Your IMC is {:.2f} and you are below of the recommended IMC.'.format(imc))
elif imc < 25:
    print('Your IMC is {:.2f} and you are with the best IMC possible.'.format(imc))
elif imc < 30:
    print('Your IMC is {:.2f} and you are above of the recommended IMC.'.format(imc))
elif imc < 40:
    print('Your IMC is {:.2f} and you have obesity.'.format(imc))
else:
    print('Your IMC is {:.2f} and you have morbid obesity.'.format(imc))