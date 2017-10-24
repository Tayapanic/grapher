import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('2d_data.csv')
plt.hist(data, normed=True, bins='auto')
plt.show()
