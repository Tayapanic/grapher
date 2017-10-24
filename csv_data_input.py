import sys
import os
import Tkinter
import tkFont
from tkFileDialog import askopenfilename
import csv
import matplotlib.pyplot as plt
#import tkMessageBox
top=Tkinter.Tk()
top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Helvetica',weight='bold')     #defining font style for buttons


def twod_csv1():
	filename = askopenfilename()
	x = []
	y = []

	with open(filename,'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			x.append(int(row[0]))
			y.append(int(row[1]))
	plt.plot(x,y, label='Loaded from file!')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Interesting Graph\nCheck it out')
	plt.legend()
	plt.show()
    #os.system('python 2d_csv1.py')
def three_d_csv():
    os.system('python 3dcsv.py')
def hist_print():
	os.system('python bar_graph.py')
def pie_print():
	os.system('python pie_data.py')


b1=Tkinter.Button(top,text="Select 2d data : delete 2dcsv.py and 2dcsv1.py",command= twod_csv1,height=13,width=27,font=btn_font)
b2=Tkinter.Button(top,text="Select 3d data : 3dcsv.py running",command= three_d_csv,height =13,width=27,font=btn_font)
b3=Tkinter.Button(top,text="Select Data : bar_graph.py running",command= hist_print,height =13,width=27,font=btn_font)
b4=Tkinter.Button(top,text="Select Data : pie_data.py running",command= pie_print,height =13,width=27,font=btn_font)


quit_bt = Tkinter.Button(master=top, text='Quit', command=sys.exit,height =13,width=27,font=btn_font)

b1.grid(row=0,column=0)
b2.grid(row=0,column=2)
b3.grid(row=1,column=0)
b4.grid(row=1,column=2)
quit_bt.grid(row=2,column=1)
top.mainloop()
