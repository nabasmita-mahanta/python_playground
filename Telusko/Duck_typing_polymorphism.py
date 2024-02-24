# Polymorphism means one thing with multiple forms.
# Polymorphism include >> Duck Typing >> Operator Overloading >> Method Overloading >> Method Over riding

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
