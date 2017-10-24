'''from sympy import Point, Line
p1, p2 = Point(1, 0), Point(5, 3)
l1 = Line(p1, p2)
l1.arbitrary_point()
Point2D(4*t + 1, 3*t)
'''
from sympy import Point3D, Line3D
from sympy.plotting import plot
p1, p2 = Point3D(1, 0, 0), Point3D(5, 3, 1)
l1 = Line3D(p1, p2)
plot(l1)
l1.arbitrary_point()
Point3D(4*t + 1, 3*t, t)
