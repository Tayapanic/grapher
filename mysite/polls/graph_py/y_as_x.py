from sympy import *
from sympy.plotting import plot
def y_as_x_graph(function,x1,x2):
	x=symbols('x')
	#function=input(": ")
	p3 = plot(function,(x,x1,x2),show=False,ylabel=str(function))
	p3.save('polls/static/polls/y_as_x.png')
	#fig_y_as_x=mpld3.fig_to_html(plt.figure(1))
	#plt.close()
	#return fig_y_as_x
#k=input()
#y_as_x(k)
