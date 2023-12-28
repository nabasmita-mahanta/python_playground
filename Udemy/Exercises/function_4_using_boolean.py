# Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.

def myfunc(x, y, z):
    if z == True:
        return x
    elif z == False:
        return y


print(myfunc("hello", "Goodbye", False))
