# Guess the output

name = 'Telusko'

print(name[-3])

# Delete the values (95,14,12)

nums = [25, 36, 95, 14, 12, 26]

del nums[2:5]

print(nums)

# dictionary

data = {1: 'Naba', 2: 'Abhi', 3: 'Puku'}

print(data[3])

print(data.get(1))

print(data.get(4, 'Not found'))

# Create dictionary with the help of list

keys = ['emmu', 'puku', 'kunu']
values = ['python', 'java', 'js']

data = dict(zip(keys, values))
print(data)

# add value

data['kemmu'] = 'python'

print(data)

# List dic inside a dic

prog = {1:'xy', 2:'po',3:['x','y','z'],4:{5:'gh',6:'jk'}}

print(prog)
print(prog[1])
print(prog[3])
print(prog[4][5])
