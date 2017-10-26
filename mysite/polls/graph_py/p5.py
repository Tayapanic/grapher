from sympy import *
from sympy.plotting import plot3d_parametric_line

u = symbols('u')
x=raw_input("input x in terms of 1 parameter : ")
y=raw_input("input y in terms of 1 parameter : ")
z=raw_input("input z in terms of 1 parameter : ")
lu=input("lower limit of u :")
uu=input("upper limit of u :")
p1=plot3d_parametric_line(x,y,z,(u,lu,uu))