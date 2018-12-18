produto = 'soccer ball'
normalPrice = float(input('What is the price of this {} ? \n'.format(produto)))
paymentCondition = int(input('In how many times you whant to pay? (0 to pay at sight) \n'))

if paymentCondition == 0:
    print('You will pay ${:.2f}'.format(normalPrice - normalPrice / 100 * 10))
elif paymentCondition == 1:
    print('You will pay ${:.2f}'.format(normalPrice - normalPrice / 100 * 5))
elif paymentCondition == 2:
    print('You will pay ${:.2f}'.format(normalPrice))
else:
    print('You will pay ${:.2f}'.format(normalPrice + normalPrice / 100 * 20))