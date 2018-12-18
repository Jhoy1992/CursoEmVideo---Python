grade1 = float(input('Type your first grade: '))
grade2 = float(input('Type your second grade: '))

average = (grade1 + grade2) / 2

if average < 5:
    print('Sorry , you have been disapproved! You average grade is {:.2f}'.format(average))
elif average >= 7:
    print('Congratulations, you have been approved! You average grade is {:.2f}'.format(average))
else:
    print('You got exam, we recommend you to study harder! You average grade is {:.2f}'.format(average))
