from sympy import *
from sympy.plotting import plot3d_parametric_line
import Tkinter
import tkFont
import sys
import os
from tkMessageBox import *
#from sympy.plotting import plot
from tkColorChooser import askcolor 
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa',weight='bold')
result=((17, 235, 224), '#11ebe0')   #default line_colour
t = symbols('t')

def func_gui():
	x=funx.get()
	y=funy.get()
	z=funz.get()
	p1=plot3d_parametric_line(x,y,z,(t, l_t.get(), u_t.get()), show=false)
	p1[0].line_color=result[1]
	p1.show()

def line_color():
    global result 
    result = askcolor(color="#6A9662",title = "Chose a color")
def callback():
	sys.exit()
funx = Tkinter.StringVar()
funy = Tkinter.StringVar()
funz = Tkinter.StringVar()
l_t = Tkinter.DoubleVar()
u_t = Tkinter.DoubleVar()
#x_lab = Tkinter.StringVar()
#y_lab = Tkinter.StringVar()
tit = Tkinter.StringVar()

l1 = Tkinter.Label(top, text="Enter x-cordinate in terms of t",font=btn_font, borderwidth=2)
l2 = Tkinter.Label(top, text="Enter y-cordinate in terms of t",font=btn_font, borderwidth=2)
l3 = Tkinter.Label(top, text="Enter z-cordinate in terms of t",font=btn_font, borderwidth=2)
l4 = Tkinter.Label(top, text="Lower limit of t",font=btn_font, borderwidth=2)
l5 = Tkinter.Label(top, text="Upper limit of t",font=btn_font, borderwidth=2)
#l6 = Tkinter.Label(top, text="X-label",font=btn_font, borderwidth=2)
#l7 = Tkinter.Label(top, text="y-label",font=btn_font)
l8 = Tkinter.Label(top, text="Title of graph",font=btn_font)
l9 = Tkinter.Label(top, text="Chose a Line-colour",font=btn_font)

funcx = Tkinter.Entry(top,textvariable=funx)
funcy = Tkinter.Entry(top,textvariable=funy)
funcz = Tkinter.Entry(top,textvariable=funz)
low_t = Tkinter.Entry(top,textvariable=l_t)
#v = Tkinter.IntVar()
upper_t = Tkinter.Entry(top,textvariable=u_t)#,text=v)
#v.set(10)
#x_label = Tkinter.Entry(top,textvariable=x_lab)
#x_label.insert(0,'x-axis')
#y_label = Tkinter.Entry(top,textvariable=y_lab)
#y_label.insert(0,'y-axis')
title = Tkinter.Entry(top)#,textvariable=tit)
#title.insert(0,'Grapher')
chose_color=Tkinter.Button(top,text='Choose a Line-colour',command=line_color)
submit_btn = Tkinter.Button(top, text="Submit", command=func_gui,font=btn_font)
quit_bt = Tkinter.Button(master=top, text='Quit', command=callback,font=btn_font,width=6)

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
l8.grid(row = 5, column = 0)
title.grid(row = 5, column = 1)
l9.grid(row=6,column=0)
chose_color.grid(row=6,column=1)


submit_btn.grid(row = 6, column = 4)
quit_bt.grid(row=7,column=4)

top.mainloop()