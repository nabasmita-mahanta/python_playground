# Guess the output

name = 'Telusko'

print(name[-3])

# Delete the values (95,14,12)

nums = [25, 36, 95, 14, 12, 26]

del nums[2:5]

print(nums)

# dictionary

data = {1: 'Naba', 2: 'Abhi', 3: 'Puku'}

print(data[3])

print(data.get(1))

print(data.get(4, 'Not found'))

# Create dictionary with the help of list

keys = ['emmu', 'puku', 'kunu']
values = ['python', 'java', 'js']

data = dict(zip(keys, values))
print(data)

# add value

data['kemmu'] = 'python'

print(data)

# List dic inside a dic

prog = {1: 'xy', 2: 'po', 3: ['x', 'y', 'z'], 4: {5: 'gh', 6: 'jk'}}

print(prog)
print(prog[1])
print(prog[3])
print(prog[4][5])

# Variable
num = 5
print(id(num))

name = 'Nabasmita'
print(id(name))

# if we have the same value but in different boxes like a, b the address will be same
# as long as the value is same
a = 10
b = a
print(id(a))
print(id(b))
print(id(10))
print(type(a))

# Different data types
# Numeric data types >> Int, Float, Complex, Bool
# Complex
num = 6 + 9j
print(type(num))

a = 6
b = 7
c = complex(a, b)
print(c)

# boolean
bool = a < b
print(bool)

# Operators
# Assignment operator
x = 8
x += 2
print(x)

a, b = 3, 4
print(a)
print(b)

# Unary Operators
n = 7
n = -n
print(n)

# Relational operator
print(a < b)
print(a == b)
print(a != b)

# Logical Operator >> and,or,not
# Arithmetic Operator >> '+','-','*' etc

# Number system conversion in python
# Decimal to binary
print(bin(25))
# Binary to decimal
print(0b11001)
# Decimal to Octal
print(oct(25))
# Decimal to Hexadecimal
print(hex(25))

# Swap two variable
# First method>> using 3rd variable
a = 5
b = 6
temp = a
a = b
b = temp

print(a)
print(b)

# 2nd Method >> without using 3rd variable

a = 5
b = 6

a = a + b  # 11
b = a - b  # 5
a = a - b  # 6

print(a)
print(b)

# 3rd method >> using XOR symbol
a = 5
b = 6

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)

# 4th Method
a = 5
b = 6

a, b = b, a
print(a, b)

# Bitwise Operator
# Complement Operator (~) #tilde
print(~12)
# Bitwise And operator (&)
print(12 & 13)
# Bitwise Or operator (|)
print(12 | 13)
# Bitwise XOR Operator (^)
print(12 ^ 13)
# Left Shift (<<)
print(10 << 2)
# Right Shift (>>)
print(10 >> 2)

# Math functions
import math

print(math.sqrt(25))
print(math.floor(2.9))
print(math.ceil(2.2))
print(math.pow(3,2))
print(math.pi)
print(math.e)


# User Input
# Char
ch = input("Enter a character: ")[0]
print(ch)
# eval
result = eval(input("enter a char: "))
print(result)



