class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A): # Class B Inheriting or takes the Features of class A
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

class C(B): # Class C Inheriting or takes the features of both class A and B
    def feature5(self):
        print("Feature 5 is working")
    def feature6(self):
        print("Feature 6 is working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature2()
b1.feature1()
b1.feature4()
b1.feature3()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()

