# Fill in the Line class methods to accept coordinates as a pair of
# tuples and return the slope and distance of the line.
# The formula to find the distance between the two points is usually given
# by d=√((x2 – x1)² + (y2 – y1)²)
# slope (m). i.e., m = (y₂ - y₁) / (x₂ - x₁)

import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1 = int(self.coor1[0])
        x2 = int(self.coor2[0])
        y1 = int(self.coor1[1])
        y2 = int(self.coor2[1])

        a = x2 - x1
        b = y2 - y1

        dist = math.sqrt((a ** 2) + (b ** 2))
        return dist

    def slope(self):
        x1 = int(self.coor1[0])
        x2 = int(self.coor2[0])
        y1 = int(self.coor1[1])
        y2 = int(self.coor2[1])
        sl = (y2 - y1) / (x2 - x1)
        return sl


li = Line(coor1=(3, 2), coor2=(8, 10))

print(li.coor1)
print(li.coor2)
print(li.distance())
print(li.slope())

# cylinder's volume is π r² h
# surface area is 2π r h + 2π r²
class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = (self.pi) * ((self.radius) ** 2) * (self.height)
        return vol

    def surface_area(self):
        sr_area = (2*self.pi*self.radius*self.height) + (2*self.pi * (self.radius)**2)
        return sr_area



c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


