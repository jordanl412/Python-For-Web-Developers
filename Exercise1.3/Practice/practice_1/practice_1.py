a = int(input('Enter the first number: '))
b = int(input('Enter another number: '))
operator = input('Choose whether to add (+) or subtract (-) these numbers: ')

if operator == '+':
    print('The sum of these numbers is:', a+b)
elif operator == '-':
    print('The difference of these numbers is:', a-b)
else:
    print('You\'ve entered an invalid operator.')