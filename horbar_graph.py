import matplotlib.pyplot as plt
import pandas as pd
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()
data = pd.read_csv(filename, sep=',',header=None, index_col =0)
print data
data.plot(kind='barh')
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.title('Title')

plt.show()
