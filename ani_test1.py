import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import *
import Tkinter
import sys
top = Tkinter.Tk()
x = symbols('x')
formula = Tkinter.StringVar()
no_frames = Tkinter.IntVar()
l_x=Tkinter.DoubleVar()
u_x=Tkinter.DoubleVar()
l_y=Tkinter.DoubleVar()
u_y=Tkinter.DoubleVar()
def calculate(value, function):
    x = value
    return eval(function)
xdata, ydata = [], []
fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro', animated=True)
def init():
	l=l_x.get()
	u=u_x.get()
	y1=l_y.get()
	y2=u_y.get()
	ax.set_xlim(l, u)
	ax.set_ylim(y1, y2)
	return ln,
def update(frame):
	form=formula.get()
	xdata.append(frame)
	ydata.append(calculate(frame,form)) #np.sin(frame))
	ln.set_data(xdata, ydata)
	return ln,
def callback():
    sys.exit()
def func_gui():
	l=l_x.get()
	u=u_x.get()
	ani = FuncAnimation(fig, update, frames=np.linspace(l,u,no_frames.get()),init_func=init, blit=True)
	plt.show()
l1=Tkinter.Label(top,text="Function in terms of x")
l2=Tkinter.Label(top,text="Lower limit of x")
l3=Tkinter.Label(top,text="Upper limit of x")
l4=Tkinter.Label(top,text="Lower limit of y")
l5=Tkinter.Label(top,text="Upper limit of y")
l6=Tkinter.Label(top,text="Number of frames")

fun=Tkinter.Entry(top,textvariable=formula)
lx=Tkinter.Entry(top,textvariable=l_x)
lx.delete(0,'end')
lx.insert(0,0)
ux=Tkinter.Entry(top,textvariable=u_x)
ux.delete(0,'end')
ux.insert(0,3.14)
ly=Tkinter.Entry(top,textvariable=l_y)
ly.delete(0,'end')
ly.insert(0,0.0)
uy=Tkinter.Entry(top,textvariable=u_y)
uy.delete(0,'end')
uy.insert(0,2.0)
fr=Tkinter.Entry(top,textvariable=no_frames)
fr.delete(0,'end')
fr.insert(0,128)
#title = Tkinter.Entry(top,textvariable=tit)
#title.insert(0,'Grapher')
#chose_color=Tkinter.Button(top,text='Choose a Line-colour',command=line_color)
submit_btn = Tkinter.Button(top, text="Submit", command=func_gui)#,font=btn_font)
quit_bt = Tkinter.Button(master=top, text='Go Back', command=callback)#,font=btn_font,width=6)

l1.grid(row=0,column=0)
fun.grid(row=0,column=1)
l2.grid(row=1,column=0)
lx.grid(row=1,column=1)
l3.grid(row=2,column=0)
ux.grid(row=2,column=1)
l4.grid(row=3,column=0)
ly.grid(row=3,column=1)
l5.grid(row=4,column=0)
uy.grid(row=4,column=1)
l6.grid(row=5,column=0)
fr.grid(row=5,column=1)

submit_btn.grid(row=6,column=2)
quit_bt.grid(row=7,column=2)
top.mainloop()