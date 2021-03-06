import sys
import os
import Tkinter
import tkFont
from tkMessageBox import *
from sympy import *
#from sympy.plotting import plot
from sympy.plotting import plot_parametric
from tkColorChooser import askcolor  
t = symbols('t')
#import tkMessageBox
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa',weight='bold')
Diff = Tkinter.IntVar()
Diff2 = Tkinter.IntVar()
#Inte = Tkinter.IntVar()
funx = Tkinter.StringVar()
funy = Tkinter.StringVar()
l_x = Tkinter.DoubleVar()
u_x = Tkinter.DoubleVar()
x_lab = Tkinter.StringVar()
y_lab = Tkinter.StringVar()
tit = Tkinter.StringVar()
result=((17, 235, 224), '#11ebe0')   #default line_colour
#cornflowerblue

def func_gui():
    fun_x = funx.get()
    fun_y = funy.get()
    l = l_x.get()
    u = u_x.get()
    '''if Diff.get():
		p1 = plot(diff(fun_y,fun_x),('t',l,u),show=false)
		p1[0].line_color=result[1]
		p1.show()
        print diff(fun_x,t)
        print diff(fun_y,t)
    elif Diff2.get():
    	p2 = plot(diff(fun_x,fun_y),('t',l,u),show=false)
    	p2[0].line_color=result[1]
    	p2.show()
    else :'''
    p3 = plot_parametric(fun_x,fun_y,('t',l,u),show=false,title=tit.get(),xlabel=x_lab.get(),ylabel=y_lab.get()) 
    p3[0].line_color=result[1]
    p3.show()

def line_color():
    global result 
    result = askcolor(color="#6A9662",title = "Chose a color")     #from tkColorChooser

def callback():
    #if askyesno('Verify', 'Really quit?'):   # from tkMessageBox
    	sys.exit()
  	
l1 = Tkinter.Label(top, text="Enter y-cordinate terms of t",font=btn_font, borderwidth=2)
l2 = Tkinter.Label(top, text="Enter x-cordinate terms of t",font=btn_font, borderwidth=2)
l3 = Tkinter.Label(top, text="Lower limit of x",font=btn_font, borderwidth=2)
l4 = Tkinter.Label(top, text="Upper limit of x",font=btn_font, borderwidth=2)
l5 = Tkinter.Label(top, text="X-label",font=btn_font, borderwidth=2)
l6 = Tkinter.Label(top, text="y-label",font=btn_font)
l7 = Tkinter.Label(top, text="Title of graph",font=btn_font)
l8 = Tkinter.Label(top, text="Chose a Line-colour",font=btn_font)

# Create the widgets
func_y = Tkinter.Entry(top,textvariable=funy)
func_x = Tkinter.Entry(top,textvariable=funx)
low_x = Tkinter.Entry(top,textvariable=l_x)
upper_x = Tkinter.Entry(top,textvariable=u_x)
upper_x.delete(0,'end')
upper_x.insert(0,10.0)
x_label = Tkinter.Entry(top,textvariable=x_lab)
x_label.insert(0,'x-axis')
y_label = Tkinter.Entry(top,textvariable=y_lab)
y_label.insert(0,'y-axis')
title = Tkinter.Entry(top,textvariable=tit)
title.insert(0,'Grapher')
#use_diff = Tkinter.Checkbutton(top, text="Plot Differential of Y w.r.t. X",variable=Diff)
#use_diff2 = Tkinter.Checkbutton(top, text="Plot Differential of X w.r.t. Y",variable=Diff2)
chose_color=Tkinter.Button(top,text='Choose a Line-colour',command=line_color)
submit_btn = Tkinter.Button(top, text="Submit", command=func_gui,font=btn_font)
quit_bt = Tkinter.Button(master=top, text='Go Back', command=callback,font=btn_font,width=6)


l1.grid(row = 0, column = 0)
func_y.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
func_x.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0)
low_x.grid(row = 2, column = 1)
l4.grid(row = 3, column = 0)
upper_x.grid(row = 3, column = 1)
l5.grid(row = 4, column = 0)
x_label.grid(row = 4, column = 1)
l6.grid(row = 5, column = 0)
y_label.grid(row=5,column=1)
l7.grid(row=6,column=0)
title.grid(row=6,column=1)
l8.grid(row=7,column=0)
chose_color.grid(row=7,column=1)
#use_diff.grid(row=0,column=3)
#use_diff2.grid(row=1,column=3)
submit_btn.grid(row = 7, column = 4)
quit_bt.grid(row=8,column=4)

top.mainloop()