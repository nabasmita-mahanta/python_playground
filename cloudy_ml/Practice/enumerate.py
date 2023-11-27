colors = ['red','green','blue','purple']

for color in colors:
    print(color)

# If we need index in for loop we can either use range or enumerate func.
# enumerate is a built in function.

for num in range(len(colors)):
    print(colors[num],num)

for index,color in enumerate(colors):
    print(color,index)