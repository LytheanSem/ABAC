
import matplotlib.pyplot as plt
import numpy as np

# Data points
X = np.array([-4.5, -3.5, -3, -1.8, -0.2, 0.3, 1.3, 2.6, 3.8, 4.8]).reshape(-1, 1)
y = np.array([[-1.11362822],
    [-1.24394281],
    [-0.91157385],
    [0.67067171],
    [1.24891634],
    [0.7776148],
    [-0.62067303],
    [-1.41641754],
    [-0.30383694],
    [0.92323755]]).reshape(-1, 1)

# Step 1: Plotting relationship
plt.scatter(X, y, color='blue', label='Data points')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Relationship between X and y')
plt.legend()
plt.grid(True)
plt.show()

# Step 2: Computing Theta without bias
Theta = np.linalg.inv(X.T @ X) @ X.T @ y

# Step 3: Plotting initial model
y_pred_initial = X @ Theta
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred_initial, color='red', label='Initial Linear Model')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Initial Model with Computed Theta')
plt.legend()
plt.grid(True)
plt.show()

# Step 4: Including bias term
X_with_bias = np.hstack((np.ones((X.shape[0], 1)), X))
Theta_with_bias = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y
print(Theta_with_bias)

# Step 5: Plotting improved model
y_pred_improved = X_with_bias @ Theta_with_bias
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred_initial, color='red', label='Initial Linear Model')
plt.plot(X, y_pred_improved, color='green', label='Improved Linear Model')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Improved Model with Bias Term')
plt.legend()
plt.grid(True)
plt.show()
