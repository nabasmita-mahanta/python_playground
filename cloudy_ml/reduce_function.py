# The reduce function is an inbuilt function in python
# It's defined in functools modules.
# that takes in a function and a sequence / iterable(list,set,dict,tuple)

# syntax - reduce(function , iterable)

# the reduce function applies the
# particular function to all the list elements

# Working :
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and
# the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

import functools

nums = [2, 3, 6, 7, 8]


def add(x, y):
    return (x + y)


result = functools.reduce(add, nums)
print(result)
print(type(result))

