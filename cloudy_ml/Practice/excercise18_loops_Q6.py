# Q6. Write a program to
# find the sum of the digits of a number accepted from the user.

num = input("please enter a number: ")
sum = 0
print(type(num))
for letter in num:
    sum = sum + int(letter)
print(sum)
