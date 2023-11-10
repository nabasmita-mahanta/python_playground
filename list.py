mylist = ['Mango', 'Apple', 'Banana']
print(mylist)
print(type(mylist))
print(mylist[0])
first_element = mylist[0]
print(first_element)
mylist[0] = 'Tomato'
print(mylist)
mylist.append('Cucumber')
print(mylist)
mylist_two = ['Onion', 'Cabbage', 'Brinjal', 'Tomato']
print(mylist + mylist_two)
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print(thislist[:4])
print(len(thislist))
thislist = ["apple", "banana", "cherry"]
if "cherry" in thislist:
    print("Yes, 'cherry' is in the fruits list")
else:
    print("No, it is not in the list")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:5] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
thislist.reverse()
thislist.append('orange')
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[-1]
print(thislist)

thislist = ["1", "2", "3"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x, end='\t')

for index in range(len(thislist)):
    print(thislist[index])

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
newthislist = thislist.copy()
thislist[0] = "apple"
print(newthislist)
