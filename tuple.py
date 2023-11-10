thistuples = (1,)
print(thistuples)
print(type(thistuples))

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#tuple unpacking
fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(x)
print(y)
print(z)
#asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print(type(red))

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#loops in tuple
thistuple = ("apple", "banana", "cherry")
for index in range(len(thistuple)):
    print(thistuple[index])

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)