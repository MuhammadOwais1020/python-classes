again = 'y'

while again.upper() == 'Y':
    x = int(input('Enter the first number: '))
    y = int(input(('Enter the second number: ')))

    command = (input('inter operator'))


    if command == '+':
        print('x + y = ' , (x +y))
    elif command == '-': 
        print('x - y = ' , (x-y))
    elif command == '*':
        print('x * y = ' , (x*y))
    elif command == '/':
        print('x / y =', x/y)
    elif command == '**':
        print('x * y = ' , x**y)
    elif command == '%':
        print('x % y = ', x%y)
    elif command == '//':
        print('x // y =' , x//y)
    else:
        print('invalid cmmand')
    
    again = input("do you want to continue y/n: ")
