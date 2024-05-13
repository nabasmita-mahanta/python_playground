# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("There was a type error!")
