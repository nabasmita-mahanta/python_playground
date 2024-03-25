# Polymorphism means one thing with multiple forms.
# Polymorphism include >> Duck Typing >> Operator Overloading >> Method Overloading >> Method Over riding


# 4 types of polymorphism

# different classes having same method name - duck typing

# child class overrides parent class method with same name - method overriding

# operators like '+' and '*' can behave differently based on what we use them for (eg 3*2=6 and python*3=pythonpythonpython)- operator overloading

# method overloading (NOT PRESENT IN PYTHON) - when in a same class we have same method names but with differnt parameters

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
