# Define a function called myfunc that
# takes in an arbitrary number of arguments, and returns the sum of those arguments.

def myfunc(*args):
    return sum(args)


print(myfunc(5, 6, 7))

