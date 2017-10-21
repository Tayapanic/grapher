#import tkinter as tk
#from tkinter.simpledialog import askstring, askinteger
#from tkinter.messagebox import showerror

import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter.simpledialog import askstring, askinteger
    from Tkinter.messagebox import showerror
else:
    import tkinter as tk
    from tkinter.simpledialog import askstring, askinteger
    from tkinter.messagebox import showerror
def display_1():
    # .get is used to obtain the current value
    # of funct widget (This is always a string)
    print(funct.get())

def display_2():
    num1 = low_x.get()
    num2 = upper_x.get()
    func = funct.get()
    label_x = x_label.get()
    label_y = y_label.get()
    tit = title.get()
    # Try convert a str to int
    # If unable eg. int('hello') or int('5.5')
    # then show an error.
    try:
       num1 = int(num1)
       num2 = int(num2)
    # ValueError is the type of error expected from this conversion
    except ValueError:
        #Display Error Window (Title, Prompt)
        showerror('Non-Int Error', 'Please enter an integer')
    else:
        print(num1)
        print(num2)
        print(func)
        print(label_x)
        print(label_y)
        print(tit)

# Create the main window
root = tk.Tk()
#label
l1 = tk.Label(root, text="Enter function y in terms of x")
l2 = tk.Label(root, text="Lower limit of x")
l3 = tk.Label(root, text="Upper limit of x")
l4 = tk.Label(root, text="X-label")
l5 = tk.Label(root, text="y-label")
l6 = tk.Label(root, text="Title of graph")


# Create the widgets
funct = tk.Entry(root)
low_x = tk.Entry(root)
upper_x = tk.Entry(root)
btn_2 = tk.Button(root, text = "Submit", command = display_2)
x_label = tk.Entry(root)
y_label = tk.Entry(root)
title = tk.Entry(root)

# Grid is used to add the widgets to root
# Alternatives are Pack and Place
l1.grid(row = 0, column = 0)
funct.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
low_x.grid(row = 1, column = 1)
l3.grid(row = 2, column = 0)
upper_x.grid(row = 2, column = 1)
l4.grid(row = 3, column = 0)
x_label.grid(row = 3, column = 1)
l5.grid(row = 4, column = 0)
y_label.grid(row = 4, column = 1)
l6.grid(row = 5, column = 0)
title.grid(row = 5, column = 1)
btn_2.grid(row = 6, column = 3)

root.mainloop()