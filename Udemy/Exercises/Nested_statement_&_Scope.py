'''
 Global variable and local variable. LEGB Role format.
 LEGB = Local, Enclosing function locals, Global, Built-in
 L: Local - Names assigned it anyway within a function(def or lambda),
 and not declared global in that function. Example: Lambda num:num**2 - num here is the local.
 E: Enclosing function locals - Names in the local scope of any and all enclosing
 functions (def or lambda), from inner to outer.
 G: Global (module) - Names assigned at the top-level of a module file, or
 declared global in a def within the file.
 B: Built-in (Python)  - Names preassigned in the built-in names module: open,range,SyntaxError

'''
# GLOBAL
name = 'THIS IS GLOBAL STRING'


def greet():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'I AM LOCAL'
        print('Hello ' + name)

    hello()


greet()

x = 50


def func():
    global x
    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

print(x)
func()
print(x)
