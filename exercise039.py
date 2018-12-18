from datetime import date

currentYear = date.today().year
birthYear = int(input('What is your birth year?'))
yearsOld = currentYear - birthYear

if yearsOld > 18:
    print('You should have gone enlist already! Have passed {} year(s) from the date.'.format(yearsOld - 18))
elif yearsOld < 18:
    print('It is not time yet to enlistment. There are {} year(s) left.'.format(18 - yearsOld))
else:
    print('Go to enlistment now!!!')

