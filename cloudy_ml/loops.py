#while loop
num = 20
i = 0
while (i<10):
    num= num+5
    print(num)
    i=i+1
print("execution end here")

#for loop
num1= 100
for i in range(0,10):
    num1=num1+100
    print(num1)
#nested loop
for i in range(1,5,2):
    for j in range(3,1,-1):
        print('(i , j)',i,j)

num = 5
while num>0:
    print(num,end=" ")
    num-=2
else:
    print("loop finish")

for i in range(1,5):
    print(i,end=" ")
    if i == 2:
        break
    else:
        print('loop finish')