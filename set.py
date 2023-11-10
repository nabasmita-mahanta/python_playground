mysets = {'Naba','Abhi','Junmoni'}
print(mysets)
mysets = {'Naba','Abhi','Junmoni','Naba'}

thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)

mysets = {'Naba','Abhi','Junmoni','Naba'}
print(len(mysets))

thisset = {"apple", "banana", "cherry"}
print("Papaya" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add('Papaya')
print(thisset)

thisset = {"apple", "banana", "cherry"}
mysets = {'Naba','Abhi','Junmoni','Naba'}
thisset.update(mysets)
print(thisset)

thisset = {"apple", "banana", "cherry"}
if 'banana' in thisset:
    thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
for every_element in thisset:
  print(every_element)

set1 = {1,2,3}
set2 = {'a','b','c'}
print(set1.union(set2))

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)