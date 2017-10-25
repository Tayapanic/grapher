from sympy import *
from sympy.plotting import plot3d_parametric_surface
import Tkinter
import tkFont
import sys
import os
from tkMessageBox import *
from tkColorChooser import askcolor 
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa',weight='bold')
result=((17, 235, 224), '#11ebe0')   #default line_colour
u = symbols('u')
v = symbols('v')

funx = Tkinter.StringVar()
funy = Tkinter.StringVar()
funz = Tkinter.StringVar()
l_t = Tkinter.DoubleVar()
u_t = Tkinter.DoubleVar()
l_v = Tkinter.DoubleVar()
u_v = Tkinter.DoubleVar()
tit = Tkinter.StringVar()

def func_gui():
    x=funx.get()
    y=funy.get()
    z=funz.get()
    p1=plot3d_parametric_surface(x,y,z,(u, l_t.get(), u_t.get()),(v,l_v.get(),u_v.get()),title=tit.get())#,xlabel=x_lab.get(),ylabel=y_lab.get())
def callback():
    sys.exit()

l1 = Tkinter.Label(top, text="Enter x-cordinate in terms of parameters u and v",font=btn_font, borderwidth=2)
l2 = Tkinter.Label(top, text="Enter y-cordinate in terms of parameters u and v",font=btn_font, borderwidth=2)
l3 = Tkinter.Label(top, text="Enter z-cordinate in terms of parameters u and v",font=btn_font, borderwidth=2)
l4 = Tkinter.Label(top, text="Lower limit of u",font=btn_font, borderwidth=2)
l5 = Tkinter.Label(top, text="Upper limit of u",font=btn_font, borderwidth=2)
l6 = Tkinter.Label(top, text="Lower limit of v",font=btn_font, borderwidth=2)
l7 = Tkinter.Label(top, text="Upper limit of v",font=btn_font, borderwidth=2)
l8 = Tkinter.Label(top, text="Title of graph",font=btn_font)

funcx = Tkinter.Entry(top,textvariable=funx)
funcy = Tkinter.Entry(top,textvariable=funy)
funcz = Tkinter.Entry(top,textvariable=funz)
low_t = Tkinter.Entry(top,textvariable=l_t)
upper_t = Tkinter.Entry(top,textvariable=u_t)#,text=v)
upper_t.delete(0,'end')
upper_t.insert(0,10.0)
low_v = Tkinter.Entry(top,textvariable=l_v)
upper_v = Tkinter.Entry(top,textvariable=u_v)
upper_v.delete(0,'end')
upper_v.insert(0,10.0)
title = Tkinter.Entry(top)
title.insert(0,'Grapher')
submit_btn = Tkinter.Button(top, text="Submit", command=func_gui,font=btn_font)
quit_bt = Tkinter.Button(master=top, text="Go Back", command=callback,font=btn_font,width=6)

l1.grid(row = 0, column = 0)
funcx.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
funcy.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0)
funcz.grid(row = 2, column = 1)
l4.grid(row = 3, column = 0)
low_t.grid(row = 3, column = 1)
l5.grid(row = 4, column = 0)
upper_t.grid(row = 4, column = 1)
l6.grid(row = 5, column = 0)
low_v.grid(row = 5, column = 1)
l7.grid(row=6,column=0)
upper_v.grid(row=6,column=1)
l8.grid(row=7,column=0)
title.grid(row=7,column=1)

submit_btn.grid(row = 7, column = 4)
quit_bt.grid(row=8,column=4)

top.mainloop()