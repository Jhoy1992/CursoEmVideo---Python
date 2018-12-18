homeValue = float(input('What is the value of the home?'))
yourIncome = float(input('What is your income?'))
howManyOfYears = int(input('How much years you want to pay?'))

installments = howManyOfYears * 12
installmentValue = homeValue / installments

if installmentValue > (yourIncome / 100 * 30):
    print('Sorry, but your incoming is to low to pay this amount!')
else:
    print('Your mensal installment will be ${:.2f} dollars.'.format(installmentValue))
    print('You will pay in {} months.'.format(installments))
