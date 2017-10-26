import sys
from pylab import *
import matplotlib.pyplot as plt,mpld3
from pylab import *
import numpy as np

#formula=input("formula:  ")

def calculate(value, function):
    x = value
    return eval(function)
def polar_graph(formula,a,b):
#a = input("initial angle as fraction of 2pi:")
#b = input("final angle as fraction of 2pi:")
	
	y = np.arange(float(a)*float(2)*np.pi, float(b)*float(2)*np.pi, .01)
	plt.polar(y, calculate(y,formula))
	plt.savefig('polls/static/polls/polar_graph.png')
	#mpld3.save_html(plt.figure(1),"test.html")
	#fig_hist=mpld3.fig_to_html(plt.figure(1))
	plt.close()
#k=input()
#a=input()
#b=input()
#polar_graph(k,a,b)
