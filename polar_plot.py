import sys
from pylab import *
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import sys
import os
import Tkinter
import tkFont
from tkColorChooser import askcolor  
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa',weight='bold')
form = Tkinter.StringVar()
l_x = Tkinter.DoubleVar()
u_x = Tkinter.DoubleVar()
#x_lab = Tkinter.StringVar()
#y_lab = Tkinter.StringVar()
tit = Tkinter.StringVar()
result=((17, 235, 224), '#11ebe0')   #default line_colour

#formula=raw_input("formula:  ")
def calculate(value, function):
    r = value
    return eval(function)  
def func_gui():
	formula=form.get()
	a = l_x.get()
	b = u_x.get()
	y = np.arange(a*np.pi, b*np.pi, .01)
	plt.polar(y, calculate(y,formula),color=result[1])
	#p1[0].line_color=result[1]
	show()

def line_color():
    global result 
    result = askcolor(color="#6A9662",title = "Chose a color")     #from tkColorChooser

def callback():
    sys.exit()
  	
l1 = Tkinter.Label(top, text="Enter formula",font=btn_font, borderwidth=2)
l2 = Tkinter.Label(top, text="Lower limit of angle as fraction of pi",font=btn_font, borderwidth=2)
l3 = Tkinter.Label(top, text="Upper limit of angle as fraction of pi",font=btn_font, borderwidth=2)
l6 = Tkinter.Label(top, text="Title of graph",font=btn_font)
l4 = Tkinter.Label(top, text="Chose a Line-colour",font=btn_font)

# Create the widgets
funct = Tkinter.Entry(top,textvariable=form)
low_x = Tkinter.Entry(top,textvariable=l_x)
low_x.delete(0,'end')
low_x.insert(0,0.0)
upper_x = Tkinter.Entry(top,textvariable=u_x)
upper_x.delete(0,'end')
upper_x.insert(0,2.0)
title = Tkinter.Entry(top,textvariable=tit)
title.insert(0,'Grapher')
chose_color=Tkinter.Button(top,text='Choose a Line-colour',command=line_color)
submit_btn = Tkinter.Button(top, text="Submit", command=func_gui,font=btn_font)
quit_bt = Tkinter.Button(master=top, text='Go Back', command=callback,font=btn_font,width=6)

l1.grid(row = 0, column = 0)
funct.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
low_x.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0)
upper_x.grid(row = 2, column = 1)
l6.grid(row = 5, column = 0)
title.grid(row = 5, column = 1)
l4.grid(row=6,column=0)
chose_color.grid(row=6,column=1)

submit_btn.grid(row = 6, column = 4)
quit_bt.grid(row=7,column=4)

top.mainloop()