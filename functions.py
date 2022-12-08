# A fucntion is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

x = int(input('Enter the first number: '))
y = int(input(('Enter the second number: ')))

command = (input('inter operator'))
result = ""

if command == '+':
    result = add(x, y)
elif command == '-': 
    result = sub(x, y)
elif command == '*':
    result = mul(x, y)

print(f"Result is {result}")





