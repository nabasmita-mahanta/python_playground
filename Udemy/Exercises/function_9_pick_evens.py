# Define a function called myfunc that takes in an arbitrary number of arguments,
# and returns a list containing only those arguments that are even.

def myfunc(*args):
    my_list = []
    for num in args:
        if num % 2 == 0:
            my_list.append(num)
        else:
            pass
    return my_list


print(myfunc(5, 6, 8, 9))
