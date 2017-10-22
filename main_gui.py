import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def twod_csv1():
    os.system('python 2d_csv1.py')
def three_d_csv():
    os.system('python 3dcsv.py')

b1=Tkinter.Button(top,text="Select 2d data : 2d_cs1.py running",command= twod_csv1)
b2=Tkinter.Button(top,text="Select 3d data : 3dcsv.py running",command= three_d_csv)
b1.grid(row=0,column=0)
b2.grid(row=1,column=0)
top.mainloop()
