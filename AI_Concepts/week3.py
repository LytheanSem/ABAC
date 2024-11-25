import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg

X = np.array([-3,-1,0,1,3]).reshape(-1,1)
y = np.array([-1.2, -0.7 ,0.14, 0.67, 1.67]).reshape(-1,1)
 
plt.figure()
plt.plot(X,y,'+',markersize =10, label='Data Points')
plt.xlabel('X axis ($x$)')
plt.ylabel('Y axis ($y$)')
plt.title("Plot of Training Data Set")
plt.xlim([-5,5])
plt.legend()
plt.grid(True)
plt.show()