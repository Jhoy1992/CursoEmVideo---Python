distance = int(input('What is the distance to your destiny?'))
if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45

print('You will pay ${0:.2f} for this trip.'.format(price))