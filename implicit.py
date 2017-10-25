from sympy import *
#from sympy import plot_implicit, cos, sin, symbols, Eq, And
from sympy.plotting import plot_implicit
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
result=((17, 235, 224), '#11ebe0') 
x= symbols('x')
y=symbols('y')
lhs=Tkinter.StringVar()
rhs=Tkinter.StringVar()
l_x = Tkinter.DoubleVar()
u_x = Tkinter.DoubleVar()
l_y = Tkinter.DoubleVar()
u_y = Tkinter.DoubleVar()
var = Tkinter.StringVar()
tit = Tkinter.StringVar()
result=((17, 235, 224), '#11ebe0') 
def func_gui():
    lh=sympify(lhs.get())
    rh=sympify(rhs.get())
    eq=var.get()
    if eq =='=':
    	p1=plot_implicit(Eq(lh,rh),(x, l_x.get(), u_x.get()), (y, l_y.get(), u_y.get()),show=false,title=tit.get())#,xlabel=x_lab.get(),ylabel=y_lab.get())
    	p1[0].line_color=result[1]
    	p1.show()
    elif eq =='>':
    	p1=plot_implicit((lh>rh),(x, l_x.get(), u_x.get()), (y, l_y.get(), u_y.get()),show=false,title=tit.get())#,xlabel=x_lab.get(),ylabel=y_lab.get())
    	p1[0].line_color=result[1]
    	p1.show()
    else :
    	p1=plot_implicit((lh<rh),(x, l_x.get(), u_x.get()), (y, l_y.get(), u_y.get()),show=false,title=tit.get())#,xlabel=x_lab.get(),ylabel=y_lab.get())
    	p1[0].line_color=result[1]
    	p1.show()

def callback():
    sys.exit()
def line_color():
    global result 
    result = askcolor(color="#6A9662",title = "Chose a color") 

l1 = Tkinter.Label(top, text="LHS",font=btn_font, borderwidth=2)
l2 = Tkinter.Label(top, text="RHS",font=btn_font, borderwidth=2)
l3 = Tkinter.Label(top, text="Lower limit of x",font=btn_font, borderwidth=2)
l4 = Tkinter.Label(top, text="Upper limit of x",font=btn_font, borderwidth=2)
l5 = Tkinter.Label(top, text="Lower limit of y",font=btn_font, borderwidth=2)
l6 = Tkinter.Label(top, text="Upper limit of y",font=btn_font, borderwidth=2)
l7 = Tkinter.Label(top, text="Title of graph",font=btn_font)
l8 = Tkinter.Label(top, text="Chose a Line-colour",font=btn_font)

l=Tkinter.Entry(top,textvariable=lhs)
r=Tkinter.Entry(top,textvariable=rhs)
var.set("=") # initial value
Lb1 = Tkinter.OptionMenu(top, var, ">", "<", "=")
low_x = Tkinter.Entry(top,textvariable=l_x)
upper_x = Tkinter.Entry(top,textvariable=u_x)#,text=v)
upper_x.delete(0,'end')
upper_x.insert(0,10.0)
low_y = Tkinter.Entry(top,textvariable=l_y)
upper_y = Tkinter.Entry(top,textvariable=u_y)
upper_y.delete(0,'end')
upper_y.insert(0,10.0)
title = Tkinter.Entry(top)
title.insert(0,'Grapher')
chose_color=Tkinter.Button(top,text='Choose a Line-colour',command=line_color)
submit_btn = Tkinter.Button(top, text="Submit", command=func_gui,font=btn_font)
quit_bt = Tkinter.Button(master=top, text='Go Back', command=callback,font=btn_font,width=6)

l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l.grid(row=1,column=0)
r.grid(row=1,column=2)
Lb1.grid(row=1,column=1)
low_x.grid(row = 2, column = 1)
l3.grid(row = 2, column = 0)
upper_x.grid(row = 3, column = 1)
l4.grid(row = 3, column = 0)
low_y.grid(row = 4, column = 1)
l5.grid(row = 4, column = 0)
upper_y.grid(row = 5, column = 1)
l6.grid(row = 5, column = 0)
title.grid(row = 6, column = 1)
l7.grid(row=6,column=0)
chose_color.grid(row=7,column=1)
l8.grid(row=7,column=0)
submit_btn.grid(row = 7, column = 4)
quit_bt.grid(row=8,column=4)
top.mainloop()