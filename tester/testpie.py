import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter.simpledialog import askstring, askinteger
    from Tkinter.messagebox import showerror
else:
    import tkinter as tk
    from tkinter.simpledialog import askstring, askinteger
    from tkinter.messagebox import showerror
#def display_1():
    # .get is used to obtain the current value
    # of funct widget (This is always a string)
#    print(funct.get())

'''def check_for_int(num):
    try:
        num = int(num)
    except ValueError:
        showerror('Non-Int Error', 'Please enter an integer')
    else:
        return 1'''
ar = []
ar2 = []
var2 = tk.IntVar()
var3 = tk.StringVar()
def submit_label():
    lab = var3.get()
    per = var2.get() 
    try:
        num = n_ent.get()
        num = int(num)
    except ValueError:
        showerror('Non-Int Error', 'Please enter an integer')
    else:
        ar.append(lab)
        ar2.append(per)

def create_window():
    top = tk.Toplevel()
    top.title(" ")
    var1 = tk.IntVar()
    label1 = tk.Label(top, text ="Enter Label name")
    names = tk.Entry(top)
    label2 = tk.Label(top, text ="Enter Percentage of label")
    percentage = tk.Entry(top)
    radio=tk.Checkbutton(top, text="Explode",variable=var1)
    btns = tk.Button(top,text="submit", command = submit_label)
    label1.grid(row=0,column=0)
    names.grid(row=0,column=1)
    label2.grid(row=1,column=0)
    percentage.grid(row=1,column=1)
    radio.grid(row=2,column=1)
    btns.grid(row=3,column=1)

def display_2():
    try:
        num = n_ent.get()
        num = int(num)
    except ValueError:
        showerror('Non-Int Error', 'Please enter an integer')
    else:
        for c in range(1,num+1):
            #window = tk.Toplevel(root)
            create_window()
            #tk.Label(top, text="Label name")

# Create the main window
root = tk.Tk()
#label
l1 = tk.Label(root, text="Enter number of labels")
l2 = tk.Label(root, text="Title of graph")
btn = tk.Button(root,text="submit", command = display_2)
n_ent = tk.Entry(root)
#if check_for_int()

# Grid is used to add the widgets to root
# Alternatives are Pack and Place
l1.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
n_ent.grid(row = 1, column = 0)
btn.grid(row = 2, column = 2)

'''colours = ['red','green','orange','white','yellow','blue']
r = 0
for c in colours:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1'''





root.mainloop()