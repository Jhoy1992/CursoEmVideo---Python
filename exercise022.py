AnyName = input('What is your name?')

print(AnyName.upper())
print(AnyName.lower())

AnyNameNoSpaces = AnyName.replace(' ', '')
print('This phrase has {} letters.'.format(len(AnyNameNoSpaces)))

AnyNameFirstName = AnyName.split()
print('The first name has {} letters.'.format(len(AnyNameFirstName[0])))
