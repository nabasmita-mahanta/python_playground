# Define a function called is_greater that takes in two arguments, and
# returns True if the first
# value is greater than the second, False if it is less than or equal to the second.

def is_greater(x, y):
    if x > y:
        return True
    elif x <= y:
        return False


print(is_greater(4, 5))
