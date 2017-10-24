from sympy import symbols
from sympy.plotting import plot
import sys
x = symbols('x')
func = sys.argv[1]
p1 = plot(func,(x,0,5))
'''while (True):
	x = raw_input("Do you want another plot(y/n) : ")
	if x == 'y':
		func = raw_input("type in the function : ")
		p2 = plot(func)
		p1.extend(p2)
	elif x == 'n' :
		break
	else :
		print('Please input y or n')
p1'''

		

