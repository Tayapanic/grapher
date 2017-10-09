import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

def fun(x, y):
  return x^3 + y^3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 10
xs = [i for i in range(n) for _ in range(n)]
ys = range(n) * n
zs = [fun(x, y) for x,y in zip(xs,ys)]
print xs
print ys
print zs
ax.scatter(xs, ys, zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
