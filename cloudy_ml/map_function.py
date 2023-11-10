# The map function is an inbuilt function in python
# that takes in two arguments - a function & an iterator

# syntax - map(function,iterator)

# the map function returns a map of the results
# after applying the given function to
# each element in the iterable


nums = [1,6,7,9,4,0]


def sqr(x):
    return x*x


result = map(sqr,nums)
print(list(result))

def double(x):
    return x * 2
lst = [1,2,3,4]
result = map(double,lst)
print(list(result))