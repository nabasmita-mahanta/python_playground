# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
list = st.split(" ")
print(list)
for element in list:
    if element.startswith("s") or element.startswith("S"):
        print(element)
for element in list:
    if len(element) > 1 and element[1] == 'h':
        print(element)

# Use range() to print all the even numbers from 0 to 10.

for element in range(0, 11, 2):
    print(element)
for element in range(0, 11):
    if element % 2 != 0:
        print(element)

# Use a List Comprehension to create a list of
# all numbers between 1 and 50 that are divisible by 3.

list = []
for num in range(1, 51):
    if num % 3 == 0:
        list.append(num)
print(list)

list1 = [num for num in range(1, 100) if num % 3 == 0]
print(list1)

""" Go through the string below 
and if the length of a word is even print "even!"""

st = 'Print every word in this sentence that has an even number of letters'
list = st.split(" ")
print(list)
for element in list:
    if len(element) % 2 == 0:
        print(element)

'''Write a program that prints the integers from 1 to 100. 
But for multiples of three print "Fizz" 
instead of the number, and for the multiples of 
five print "Buzz". For numbers which are multiples of both 
three and five print "FizzBuzz".'''

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

'''Use List Comprehension to create a list of 
the first letters of every word in the string below:'''

st = 'Create a list of the first letters of every word in this string'
list = st.split(" ")
print(list)
list1 =[]
for element in list:
    list1.append(element[0])
print(list1)

list2 = [element[0] for element in list]
print(list2)





