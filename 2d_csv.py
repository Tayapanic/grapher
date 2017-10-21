from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style
from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print filename
style.use('ggplot')
data = np.genfromtxt(filename, delimiter=',') #skip_header=10, skip_footer=10, names=['x', 'y', 'z'])
#x, y = np.loadtxt('filename', unpack=True,delimiter=',')
x= data[:,0]
y= data[:,1]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')

plt.show()
