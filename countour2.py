import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def hyp_part1(x,y,z):
    return (x**3) + (y**2) + (z**2) - 10000

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_range = np.arange(-100,100,10) 
y_range = np.arange(-100,100,10)
X,Y = np.meshgrid(x_range,y_range)
A = np.linspace(-100, 100, 15)

A1,A2 = np.meshgrid(A,A)    

for z in A: 
    X,Y = A1, A2
    Z = hyp_part1(X,Y,z)
    ax.contour(X, Y, Z+z, [z], zdir='z')

for y in A: 
    X,Z= A1, A2
    Y = hyp_part1(X,y,Z)
    ax.contour(X, Y+y, Z, [y], zdir='y')

for x in A:
    Y,Z = A1, A2 
    X = hyp_part1(x,Y,Z)
    ax.contour(X+x, Y, Z, [x], zdir='x')

ax.set_zlim3d(-100,100)
ax.set_xlim3d(-100,100)
ax.set_ylim3d(-100,100)

plt.show()
