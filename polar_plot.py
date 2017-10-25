import sys
from pylab import *
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from scitools.StringFunction import StringFunction
formula=raw_input("formula:  ")
def calculate(value, function):
    x = value
    return eval(function)
a = input("initial angle as fraction of 2pi:")
b = input("final angle as fraction of 2pi:")

y = np.arange(a*2*np.pi, b*2*np.pi, .01)


plt.polar(y, calculate(y,formula))
show()

