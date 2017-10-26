import sys
import os
import Tkinter
import tkFont
#from tkFileDialog import askopenfilename
import tkMessageBox
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa',weight='bold')

#cornflowerblue
def polar():
    os.system('python polar_plot.py')
def func_gui():
    os.system('python ani_test1.py')
'''def give_points():
	os.system('python misc.py')'''
def callback():
    sys.exit()

b1=Tkinter.Button(top,text="Polar Plot",command= polar,height=13,width=32,font=btn_font)
b2=Tkinter.Button(top,text="See a 2-d plot during formation",command= func_gui,height =13,font=btn_font)
#b3=Tkinter.Button(top,text="Miscellaneous Plots",command= give_points,height =13,width=27,font=btn_font)
#b4=Tkinter.Button(top,text="Select Data : pie_data.py running",command= pie_print,height =13,width=27,font=btn_font)

quit_bt = Tkinter.Button(master=top, text='Go Back', command=sys.exit,height =13,width=27,font=btn_font)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
#b3.grid(row=0,column=3)
#b4.grid(row=1,column=2)
quit_bt.grid(row=2,column=4)
top.mainloop()