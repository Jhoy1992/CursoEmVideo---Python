AnyName = input('What is your name?').strip()

print('Your name uppercase is {}'.format(AnyName.upper()))
print('Your name lowercase is {}'.format(AnyName.lower()))

AnyNameNoSpaces = AnyName.replace(' ', '')
print('This name has {} letters.'.format(len(AnyNameNoSpaces)))

AnyNameFirstName = AnyName.split()
print('The first name has {} letters. (without spaces)'.format(len(AnyNameFirstName[0])))

