from functools import reduce

# filter

nums = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

# map

doubles = list(map(lambda n: n * 2, evens))
print(doubles)

# reduce >> first we have to import reduce from functools

sum = reduce(lambda a, b: a + b, doubles)
print(sum)
