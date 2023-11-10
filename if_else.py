a = 33
b = 33
if a>b :
    print("a is greater than b")
elif a==b:
    print('a is equal to b')
else:
    print("a is not greater")
# Ternary of shorthand operators
a = 2
b = 330
print("A") if a > b else print("B")

# and operator
a = 300
b = 50
c = 200
if a>b and c>b:
    print("a and c both are greater than b")
#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
# nested if
a = 15
if a >= 10:
    print("Above ten")
    if a>20:
        print('also above 20')
    else:
        print('not above 20')
a = 5
b = 5
c = 5
if a>b and a>c:
    print('a is the highest number')
elif b>a and b>c:
    print("b is the highest number")
elif c>a and c>b:
    print("c is the highest")
else:
    pass


