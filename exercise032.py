from datetime import date

currentYear = date.today().year
year = int(input('What year you want to analize? Type 0 to select the current year.'))

if year <= 0:
    year = currentYear


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("The year {} is a leap year.".format(year))
else:
    print("The year {} is NOT a leap year.".format(year))
    
