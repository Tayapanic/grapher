import sys
import os
import Tkinter
import tkFont
#import tkMessageBox
top=Tkinter.Tk()
#top.geometry('816x870+0+0')
top.title('Grapher')
btn_font = tkFont.Font(family='Purisa')
quit_font = tkFont.Font(family='Purisa',weight='bold')

def pie_print():
    os.system('python piechart.py')
def bar_print():
    os.system('python ')
def line_print():
	os.system('python ')
def plotting():
    os.system('python ')
def scatter_print():
    os.system('python ')
#def pie_print():
#	os.system('python pie_data.py')


b1=Tkinter.Button(top,text="Pie chart",command= pie_print,height=6,width=27,font=btn_font,relief="groove",highlightcolor="black")
b2=Tkinter.Button(top,text="Bar graph",command= bar_print,height =6,width=27,font=btn_font,relief="groove")
b3=Tkinter.Button(top,text="Line Graph",command= line_print,height =6,width=27,font=btn_font,relief="groove")
b3=Tkinter.Button(top,text="Scatter Plot",command= scatter_print,height =6,width=27,font=btn_font,relief="groove")
b3=Tkinter.Button(top,text="Line Graph",command= line_print,height =6,width=27,font=btn_font,relief="groove")
#b4=Tkinter.Button(top,text="Select Data : pie_data.py running",command= pie_print,height =13,width=27,font=btn_font)


quit_bt = Tkinter.Button(master=top, text='Quit', command=sys.exit,height =9,width=27,font=quit_font,relief="groove")

b1.grid(row=1,column=0)
b2.grid(row=2,column=0)
b3.grid(row=3,column=0)
#b4.grid(row=1,column=2)
quit_bt.grid(row=4,column=1)
top.mainloop()