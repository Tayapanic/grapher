from sympy import *
from sympy.plotting import plot3d
def z_as_yx_plot(function):
	p = plot3d(function,show=False,zlabel=str(function))
	p.save('polls/static/polls/z_as_yx.png')
