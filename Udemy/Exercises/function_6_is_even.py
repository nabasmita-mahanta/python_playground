# Define a function called is_even that takes in one argument,
# and returns True if the passed-in value is even, False if it is not.

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(is_even(6))
