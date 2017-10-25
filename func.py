import sys
import os
import Tkinter
import tkFont
#from tkFileDialog import askopenfilename
#import tkMessageBox
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa',weight='bold')#,weight='bold')
label_font=tkFont.Font(size=25,slant="italic")
#cornflowerblue
def y_as_x():
    os.system('python function_gui_yasx.py')
def para_2d():
    os.system('python function_gui_para.py')
def eq_solver():
	os.system('python implicit.py')
def z_as_xy():
    os.system('python 3d_z.py')
def para_line_3d():
    os.system('python 3d_line_func.py')
def para_sur_3d():
	os.system('python 3d_parametric_surface.py')
def quit():
	sys.exit()

l1=Tkinter.Label(top,text="Draw 2d plots",font=label_font,height=2)
l2=Tkinter.Label(top,text="Draw 3d plots",font=label_font,height=2) 

bt1=Tkinter.Button(top,text="Give y as function of x",command= y_as_x,font=btn_font,width=60,height=2)
bt2=Tkinter.Button(top,text="Give y and x both in terms of parameter",command= para_2d,font=btn_font,width=60,height=2)
bt3=Tkinter.Button(top,text="Give a non-differential equation/inequation",command= eq_solver,font=btn_font,width=60,height=2)
br1=Tkinter.Button(top,text="Give z-cordinate in terms of x and y",command= z_as_xy,font=btn_font,width=60,height=2)
br2=Tkinter.Button(top,text="Give all three co-ordinates in terms of a single parameter",command= para_line_3d,font=btn_font,width=60,height=2)
br3=Tkinter.Button(top,text="Give all three co-ordinates in terms of two parameters",command= para_sur_3d,font=btn_font,width=60,height=2)

quit_bt = Tkinter.Button(master=top, text='Go Back', command=quit,font=btn_font,width=20,height=3)
l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
bt1.grid(row=1,column=0)
bt2.grid(row=2,column=0)
bt3.grid(row=3,column=0)
br1.grid(row=1,column=2)
br2.grid(row=2,column=2)
br3.grid(row=3,column=2)
quit_bt.grid(row=4,column=1)
top.mainloop()