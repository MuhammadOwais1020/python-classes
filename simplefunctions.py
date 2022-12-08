def add(x, y):
    return x + y


def sub(x, y):
    return x -y


def mul(x, y):
    return x * y


again = "y"


while again.lower() == "y":
    num1 = int(input('ENter value for x: '))
    num2 = int(input('ENter value for y: '))
    opt = input("Enter an operator")

    if opt == "+":
        result = add(num1, num2)
    elif opt == "-":
        result = sub(num1, num2)
    elif opt == "*":
        result = mul(num1, num2)

    print(f"result is: {result}")

    again = input('do you wants more calculations? y/n: ')


