class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        s4 = Student(m1,m2)
        return s4

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(58,69)
s2 = Student(60,65)
s3 = s1 + s2
s4 = s1 * s2

if s1 > s2:
    print("s1 Wins")
else:
    print("s2 Wins")

print(s3.m1)
print(s3.m2)
print(s4.m1)
print(s4.m2)
print(s1)


