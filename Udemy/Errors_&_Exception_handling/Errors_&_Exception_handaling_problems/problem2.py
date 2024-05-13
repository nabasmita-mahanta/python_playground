# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

x = 5
y = 0
try:
    z = x / y
except TypeError:
    print("There was a type error!")
except ZeroDivisionError:
    print("There was a zero division error!")
finally:
    print("All done")
