SomeText = input('Type anything: ').upper()

print('The "A" appears {} times.'.format(SomeText.count('A')))
print('The "A" appears the first time in the {} position.'.format(SomeText.find('A') +1))
print('The "A" appears the last time in the {} position.'.format(len(SomeText) - SomeText[::-1].find('A')))
