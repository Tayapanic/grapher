import csv
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

hFile = open("a.csv", 'r')
datfile = csv.reader(hFile)
dat = []

for row in datfile:
        dat.append(map(float,row))

temp = zip(*(dat))

fig = pylab.figure(figsize=pyplot.figaspect(.96))
ax = Axes3D(fig)
ax.plot_wireframe(temp[0], temp[1], temp[2])
pyplot.show()