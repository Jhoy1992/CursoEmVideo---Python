PersonName = input('Type a person name: ').upper().strip()
PersonName = PersonName.split()

print('First name: {}'.format(PersonName[0]))
print('Last name: {}'.format(PersonName[len(PersonName) -1]))