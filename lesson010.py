# age = int(input('How old are you?'))

# if age <= 15:
#     print('You are so young.')
# else: 
#     print('You are getting old.')

# Simple if condition

# print('You are so young.' if age <= 15 else 'You are getting old.')

# name = str(input('What is your name?'))
# if name == 'Gustavo':
#     print('What a beautiful name you have!')
# else:
#     print('Your name is so normal!')

# print('Good morning, {}!'.format(name))

grade1 = float(input('Type your first grade:'))
grade2 = float(input('Type your second grade:'))
average = (grade1 + grade2) / 2
print('You average grade is {}.'.format(average))
print('Your average is good!' if average > 6 else 'Your average is bad. Study more in the next time.')