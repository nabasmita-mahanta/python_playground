# Constructor : allocates the size of the object.
class Computer:
    def __init__(self):
        self.name = "Nabas"
        self.age = 26
    def update(self):
        self.age = 28

    def compare(self,other): # Compare
        if self.age == other.age:
            return  True
        else:
            return False


c1 = Computer() # Computer() refers the constructor here.
c2 = Computer()

c1.name = "Puku"
c2.update()
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
print(c1.name)
print(c2.name)
print(c2.age)

