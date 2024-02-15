class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'

s1 = Student('Naba', 8)
s2 = Student('Puku', 6)

s1.show()
s2.show()
