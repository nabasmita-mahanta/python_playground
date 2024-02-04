# An array is a special variable, which can hold more than one value at a time.
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# to work with arrays in Python you will have to import a library, like the NumPy library.
# or we have to import array first
# In array all the values should be of same type

from array import *

vals = array('i', [5, 9, -8, 4, 2])
print(vals)
print(vals[1])
for i in range(len(vals)):
    print(vals[i])
print(vals.buffer_info())  # buffer_info gives the address, size of the array
print(vals.typecode)  # type of array value
vals.reverse()
print(vals)

char = array('u', ['a', 'b', 'c'])

for c in char:
    print(c)

newArr = array(vals.typecode, (a * a for a in vals))
print(newArr)

i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1

# Taking user input for array

arr = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("enter the values here: "))
    arr.append(x)
print(arr)

# fetching index position
# method 1

val = int(input("Enter the values for search: "))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

# 2nd method
print(arr.index(val))
