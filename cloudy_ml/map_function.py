# The map function is an inbuilt function in python
# that takes in two arguments - a function & an iterator

# syntax - map(function,iterator)

# the map function returns a map of the results
# after applying the given function to
# each element in the iterable


nums = [1, 6, 7, 9, 4, 0]


def sqr(x):
    return x * x


result = map(sqr, nums)
print(list(result))


def double(x):
    return x * 2


lst = [1, 2, 3, 4]
result = map(double, lst)
print(list(result))


def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
result = map(square, my_nums)
print(list(result))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))


