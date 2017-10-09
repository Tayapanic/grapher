from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')
x, y = np.loadtxt('result.csv', unpack=True,delimiter=',')
print(x)
print(y)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')

plt.show()
