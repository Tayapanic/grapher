import sys
import os
import Tkinter
import tkFont
#from tkFileDialog import askopenfilename
from tkMessageBox import askyesno
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Helvetica',weight='bold')

#cornflowerblue
def csv_gui():
    os.system('python csv_data_input.py')
def func_gui():
    os.system('python func.py')
def give_points():
	os.system('python misc.py')
def callback():
	if askyesno('Verify', 'Really quit?'):
		sys.exit()


b1=Tkinter.Button(top,text="Import a csv file for plotting",command= csv_gui,height=13,width=27,font=btn_font)
b2=Tkinter.Button(top,text="Plot a function",command= func_gui,height =13,width=27,font=btn_font)
b3=Tkinter.Button(top,text="Miscellaneous Plots",command= give_points,height =13,width=27,font=btn_font)
#b4=Tkinter.Button(top,text="Select Data : pie_data.py running",command= pie_print,height =13,width=27,font=btn_font)


quit_bt = Tkinter.Button(master=top, text='Quit', command=callback,height =13,width=27,font=btn_font)

b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)
#b4.grid(row=1,column=2)
quit_bt.grid(row=2,column=4)
top.mainloop()