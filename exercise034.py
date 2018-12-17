salary = float(input('Type your salary: $ '))

if salary <= 1250:
    salary = salary + (salary / 100 * 15)
else:
    salary = salary + (salary / 100 * 10)

print('You salary will be ${0:.2f}'.format(salary))
