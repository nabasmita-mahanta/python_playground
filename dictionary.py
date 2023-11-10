mydictionary = {
    'name': 'Nabasmita',
    'age': 25,
    'place': 'Nazira'
}
print(mydictionary)
print(mydictionary['age'])

mydictionary = {
    'name': 'Nabasmita',
    'age': 25,
    'place': 'Nazira',
    'age': 27
}
print(mydictionary)
print(len(mydictionary))
# key and values can be of any data type
thisdict = {
    1.0: "Ford",
    2.0: False,
    ('Mango', ''): 1964,
    '': ["red", "white", "blue"]
}
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
each_key = thisdict["model"]
print(each_key)
each_key = thisdict.get("model")
print(each_key)
keys = thisdict.keys()
print(type(keys))
values = thisdict.values()
print(values)
items = thisdict.items()
print(items)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

for each_key in thisdict:
  print(each_key)

for values in thisdict:
  print(thisdict[values])

for each_key,values in thisdict.items():
    print(each_key,values)

new_dictionary = mydictionary.copy()

## Nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
x = myfamily['child2']['name']
print(x)
x = myfamily.get('child3').get('name')
print(x)



