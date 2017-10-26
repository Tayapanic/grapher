import sys
import os
import Tkinter
import tkFont
from tkFileDialog import askopenfilename
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#import tkMessageBox
top=Tkinter.Tk()
#top.geometry('816x670+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa')#,weight='bold')     #defining font style for buttons

def twod_csv1():
	filename = askopenfilename()
	x = []
	y = []
	with open(filename,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			x.append(float(row[0]))
			y.append(float(row[1]))
	plt.plot(x,y)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Grapher')
	plt.legend()
	plt.show()
def hist():
	filename = askopenfilename()
	data = np.loadtxt(filename)
	plt.hist(data, normed=True, bins='auto')
	plt.show()
def hor_bar():
	filename = askopenfilename()
	data = pd.read_csv(filename, sep=',',header=None, index_col =0)
	data.plot(kind='barh')
	plt.ylabel('Frequency')
	plt.xlabel('Words')
	plt.title('Title')
	plt.show()
def three_d_csv():
    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')
    filename = askopenfilename()
    data = csv.reader(open(filename, 'rb'), delimiter=",", quotechar='|')
    print data
    column1, column2,column3 = [], [],[]
    for row in data:
    	column1.append(float(row[0]))
    	column2.append(float(row[1]))
    	column3.append(float(row[2]))
	x= np.array(column1)
	y=np.array(column2)
	z=np.array(column3)
	print column1
	print column2
	print column3
	ax1.scatter(x,y,z)
	plt.show()
def three():
	colors = (0,0,0)
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
def bar_plot():
	filename = askopenfilename()
	data = pd.read_csv(filename, sep=',',header=None, index_col =0)
	data.plot(kind='bar')
	plt.ylabel('Frequency')
	plt.xlabel('Words')
	plt.title('Title')
	plt.show()
	#os.system('python bar_graph.py')
def pie_print():
	filename = askopenfilename()
	data = csv.reader(open(filename, 'rb'), delimiter=",", quotechar='|')
	column1, column2 = [], []

	for row in data:
		column1.append(row[0])
		column2.append(row[1])
	labels = column1
	sizes = column2
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	plt.show()

b1=Tkinter.Button(top,text="Line graph",command= twod_csv1,height=8,width=27,font=btn_font)
b2=Tkinter.Button(top,text="Horizontal Bar graph",command= hor_bar,height =8,width=27,font=btn_font)
b3=Tkinter.Button(top,text="Bar graph",command= bar_plot,height =8,width=27,font=btn_font)
b4=Tkinter.Button(top,text="Pie chart",command= pie_print,height =8,width=27,font=btn_font)
b5=Tkinter.Button(top,text="Histogram",command=hist,font=btn_font,height =8,width=27)
b6=Tkinter.Button(top,text="2d Scatter plot",command=three,font=btn_font,height =8,width=27)
quit_bt = Tkinter.Button(master=top, text='Go back', command=sys.exit,height =8,width=27,font=btn_font)

b1.grid(row=0,column=0)
b5.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=1,column=0)
b6.grid(row=1,column=1)
b4.grid(row=1,column=2)
quit_bt.grid(row=2,column=1)
top.mainloop()
