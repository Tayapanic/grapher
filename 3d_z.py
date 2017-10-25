from sympy.plotting import plot3d
import sys
import os
import Tkinter
import tkFont
from tkMessageBox import *
from sympy import *
from sympy.plotting import plot
from tkColorChooser import askcolor  
x = symbols('x')
y=symbols('y')
#import tkMessageBox
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa',weight='bold')
fun = Tkinter.StringVar()
l_x = Tkinter.DoubleVar()
u_x = Tkinter.DoubleVar()
l_y = Tkinter.DoubleVar()
u_y = Tkinter.DoubleVar()
tit = Tkinter.StringVar()
#cornflowerblue
#Verdana another font


def func_gui():
    function = fun.get()
    lx = l_x.get()
    ux = u_x.get()
    ly = l_y.get()
    uy = u_y.get()
    p3 = plot3d(function,('x',lx,ux),('y',ly,uy),title=tit.get())#,xlabel=x_lab.get(),ylabel=y_lab.get())#,show=false) 
def callback():
    	sys.exit()
  	
l1 = Tkinter.Label(top, text="Enter function Z in terms of x and y",font=btn_font, borderwidth=2)
l2 = Tkinter.Label(top, text="Lower limit of x",font=btn_font, borderwidth=2)
l3 = Tkinter.Label(top, text="Upper limit of x",font=btn_font, borderwidth=2)
l4 = Tkinter.Label(top, text="Lower limit of y",font=btn_font, borderwidth=2)
l5 = Tkinter.Label(top, text="Upper limit of y",font=btn_font)
l6 = Tkinter.Label(top, text="Title of graph",font=btn_font)

funct = Tkinter.Entry(top,textvariable=fun)
low_x = Tkinter.Entry(top,textvariable=l_x)
upper_x = Tkinter.Entry(top,textvariable=u_x)
upper_x.delete(0,'end')
upper_x.insert(0,10.0)
low_y = Tkinter.Entry(top,textvariable=l_y)
upper_y = Tkinter.Entry(top,textvariable=u_y)
upper_y.delete(0,'end')
upper_y.insert(0,10.0)
title = Tkinter.Entry(top,textvariable=tit)
title.insert(0,'Grapher')
submit_btn = Tkinter.Button(top, text="Submit", command=func_gui,font=btn_font)
quit_bt = Tkinter.Button(master=top, text='Go Back', command=callback,font=btn_font,width=6)


l1.grid(row = 0, column = 0)
funct.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
low_x.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0)
upper_x.grid(row = 2, column = 1)
l4.grid(row = 3, column = 0)
low_y.grid(row = 3, column = 1)
l5.grid(row = 4, column = 0)
upper_y.grid(row = 4, column = 1)
l6.grid(row = 5, column = 0)
title.grid(row = 5, column = 1)
submit_btn.grid(row = 6, column = 4)
quit_bt.grid(row=7,column=4)

top.mainloop()