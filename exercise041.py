from datetime import date

currentYear = date.today().year
birthYear = int(input('What is your birth year?'))
yearsOld = currentYear - birthYear

if yearsOld > 20:
    print('You category is "MASTER"! You are {} years old.'.format(yearsOld))
elif yearsOld > 19:
    print('You category is "SÊNIOR"! You are {} years old.'.format(yearsOld))
elif yearsOld > 14:
    print('You category is "JUNIOR"! You are {} years old.'.format(yearsOld))
elif yearsOld > 9:
    print('You category is "INFANTIL"! You are {} years old.'.format(yearsOld))    
else:
    print('You category is "MIRIM"! You are {} years old.'.format(yearsOld))    
