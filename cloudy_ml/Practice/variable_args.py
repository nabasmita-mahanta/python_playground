# *args (Non-Keyword Arguments)
def add(*arguments):
    total = 0
    for item in arguments:
        total = total + item
    return total


result = add(1, 7, 3, 8)
print(result)


# **kwargs (Keyword Arguments)

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key + ' == ' + str(value))


my_function(abhi=28, naba=2)
