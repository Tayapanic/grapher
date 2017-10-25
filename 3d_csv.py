from mpl_toolkits.mplot3d import Axes3D
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
data = csv.reader(open('3d_data.csv', 'rb'), delimiter=",", quotechar='|')
column1, column2,column3 = [], [],[]

for row in data:
    column1.append(float(row[0]))
    column2.append(float(row[1]))
    column3.append(float(row[2]))

x= np.array(column1)

y=np.array(column2)
z=np.array(column3)

ax1.scatter(x,y,z)
plt.show()
