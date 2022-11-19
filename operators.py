# operators
print(4 + 5)

# Python Arithmetic Operators 

# 1. Addition
print(4 + 5)

#  2. Subtraction 
print(3 - 4)

# Multiplication
print(3 * 4)

# Division
print(15 / 2)

# Modulus 
print(4 % 2)

# Exponentiation
print(3 ** 2)

# Floor Division
print(15 // 2)

# Assignment Operator 

# =
x = 5

# +=
x += 3 # x = x + 3

# -=
x -= 2 # x = x - 2

# *=
x *= 2 # x = x * 2

# /=
x /= 2 # x = x / 2

# %=
x %= 2 # x = x % 2


# //=
x //= 2 # x = x // 2

# **=
x **= 2 # x = x ** 2

# PYTHON COMPARISION OPERATOR
x = 3
y = 5
# ==, equal
print(x == y)

# !=, not equal
print(x != y)

# >, greater than 
print(x > y)

# <, Less than 
print(x < y)

# >=, greater than or equal
print(x >= y)

# <=, less than or equal 
print(x <= y)

# LOGICAL OPERATORS
x = 2
y = 3
a = 4
b = 3
# and, return true if both statements are true 
print("And logical operator: " + str((x > y and a > b)))

# or, return true if one of the statement is true
print("Or logical operator: " + str((x > y or a > b)))

# not, reverse the resut, return false if the result is true, return true is the result is false
print("Not logical operator: " + str(not(x > y or a > b)))

# condition age >= 25, status = single 

age = 24
status = "single"

if(age >= 25 and status == 'single'):
    print("Accepted for Interview")
else:
    print("Rejected")

# PYTHON INDENTITY OPERATORS
x = 5
y = x
# is, returns True if both variables are the same object
print(x is y)
# is not, returns True if both variables are not the same object 
print(x is not y)

# PYTHON MEMBERSHIP OPERATORS
# in, returns true is a sequence with the specified value is present in the object
x = ['banana', 'apple']
print('banana' in x)
# not in, returns true is a sequence with the specifeid value is not present in the object 
print("apple" not in x) 





