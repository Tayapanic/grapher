import numpy as np
import matplotlib.pyplot as plt
from tkFileDialog import askopenfilename
import csv
import Tkinter
import tkFont
#x = [1,2,3,4,5,6]#np.random.rand(N)
#y = [1,2,3,4,5,6]#np.random.rand(N)
colors = (0,0,0)
top=Tkinter.Tk()
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa')


filename = askopenfilename()
x = []
y = []
with open(filename,'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(float(row[0]))
		y.append(float(row[1]))
plt.scatter(x, y,  c=colors, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grapher')
plt.legend()
plt.show()
