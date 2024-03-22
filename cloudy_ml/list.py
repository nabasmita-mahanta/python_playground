list1 = [[2, 3], [4, 5, 6, 8], [1], 75]
print(list1)
print(len(list1[2]))

list2 = [[1, 2], [3.4], [5, 6], [7, 8]]
print(list2[-2][-1])

a = [1, 2, 3]
a.extend(a[:2])
print(a)

x = [1, 2, 3, 4, 5]
print(x[2::-1])

odd_sq = [i ** 2 for i in range(1, 11) if i % 2 == 1]
print(odd_sq)

# print the letter with and without x
var = ['apples', 'mango', 'grapes', 'banana', 'orange']
end_letters = 's'
with_s = [x for x in var if x.endswith(end_letters)]
without_s = [x for x in var if x not in with_s]

print(with_s)
print(without_s)

x = [i ** 2 for i in range(1, 6) if i % 2 == 0]
print(x)

t = (1, 2, 3)
print(t[0])
print(t.index(1))

print("----------CUSTOM SORTING")

def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]

thislist.sort(key=myfunc, reverse=True)

print(thislist)
