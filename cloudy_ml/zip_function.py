# The zip function is an inbuilt function in python
# that takes in two iterable(list,set,dict,tuple)

# syntax - zip(iterator,iterator,...)

# the zip function combines two or more iterables into a single iterable
# where elements from corresponding positions are paired together.

names = ['ram', 'syam', 'sam', 'nam', 'tam']
marks = [90, 23, 21, 78, 89]

result = zip(names,marks)
print(result)
print(type(result))
print(list(result))
