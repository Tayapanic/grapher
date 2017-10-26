from sympy import *
from sympy.plotting import plot3d_parametric_surface

def xyz_param_graph(x,y,z,lu,uu,lv,uv):
	u = symbols('u')
	v = symbols('v')
	p1=plot3d_parametric_surface(x,y,z,(u,lu,uu),(v,lv,uv))
	p1.save('polls/static/polls/xyz_param.png')


#x=input("input x in terms of 2 parameters : ")
#y=input("input y in terms of 2 parameters : ")
#z=input("input z in terms of 2 parameters : ")
#lu=float(input("lower limit of u :"))
#uu=float(input("upper limit of u :"))
#lv=float(input("lower limit of v :"))
#uv=float(input("upperlimit of v :"))
#xyz_param_graph(x,y,z,lu,uu,lv,uv)
