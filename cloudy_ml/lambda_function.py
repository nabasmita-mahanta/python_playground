def sqr(num):
    return num * num


result = sqr(5)
print(result)

# Lambda functions are also called anonymous functions.

result = lambda x, y, z: x + y + z
print(result(6, 7, 8))

# Functions can be treated as objects and assigned to variables

# def shout(text):
#    return text.upper()


shout = lambda t: t.upper()

print(shout('Hello'))

yell = shout
print(yell('heloooooooooooo'))

# Passing function as an argument-Higher order function

# def whisper(text):
#     return text.lower()


whisper = lambda t: t.lower()

print(whisper('Please Keep QUIET'))

# def greet(fn):
#     # storing the function in a variable
#     greeting = fn('Hey there, PYTHON is awesome')
#     return greeting


greet = lambda fn: fn('Hey there, PYTHON is awesome')

print(greet(shout))
print(greet(lambda t: t.lower()))

# def sqr(num):
#     return num**2
# print(sqr(3))

sqr = lambda num: num ** 2
print(sqr(5))


