from sympy import symbols
from sympy.plotting import plot
import sympy
x = symbols('x')

#Defined the function to be differentiated
f = sympy.exp(x) * sympy.sin(2*x)
#plot1 = f
p1 = f
#plot2 = f'
p2 = sympy.diff(f, x)
#P is the plot of f and f'
p = plot(p1, p2, (x, 0, 10))
#change the color of p2
p[1].line_color = 'r'

p.show()