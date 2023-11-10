# Q2. Given a list of numbers.
# Print the sum of all the positive numbers.
numbers = [-5,-7,0,9,5,-1,4]
sum=0
for num in numbers:
    if num>=0:
        sum=sum+num
print(sum)

