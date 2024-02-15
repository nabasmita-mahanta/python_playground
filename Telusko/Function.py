# Formal argument : When we are defining a value is called formal argument.
# Actual Argument : when we are calling a value is called actual argument.
# Actual Argument >> Position, Keyword, Default, Variable Length

# Variable Length argument example
def sum(a, *b):
    print(a)
    print(b)

    for i in b:
        c = a + i
    print(c)


sum(3, 4, 5, 7)


# Kwargs = Keyword Variable Length Argument

def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('Nabasmita', age=25, city='Dib', mob=97066)
