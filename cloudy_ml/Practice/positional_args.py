def welcome(x,y):
    print(f'Hello {x} welcome to {y}')


# this is positional argument
welcome('Naba', 'earth')

# this is keyword argument
welcome(y='earth', x='Naba')
welcome('Naba', y='earth')

# welcome(x='Naba', 'earth') error:: Positional argument after keyword argument
