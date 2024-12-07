import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg

X = np.array([-4.5, -3.5, -3, -1.8, -0.2, 0.3, 1.3, 2.6, 3.8, 4.8]).reshape(-1,1) # 10x1 vector, N=5, D=1
y = np.array([
    [-1.11362822],
    [-1.24394281],
    [-0.91157385],
    [0.67067171],
    [1.24891634],
    [0.7776148],
    [-0.62067303],
    [-1.41641754],
    [-0.30383694],
    [0.92323755]
]).reshape(-1,1) # 10x1 vector


# Create a plot to display data and predictions
plt.figure()
# Plot original data points
plt.plot(X, y, '+', markersize=10, label='Data points')
# Plot line of best fit
plt.xlabel("X-axis ($x$)")  # Label the x-axis
plt.ylabel("Y-axis ($y$)")  # Label the y-axis
plt.title("Relation between X and Y")  # Title for the plot
plt.legend()  # Display legend
plt.grid(True)  # Show grid
# plt.show()  # Display the plot


# Define function to calculate theta
def max_lik_estimate(X, y):
    # Calculate the inverse of X transposed times X
    inverse_term = np.linalg.inv(X.T @ X)
    # Multiply the inverse by X transposed, and then by y to compute theta maximum likelihood
    theta_ml = inverse_term @ (X.T @ y)
    return theta_ml

# Calculate theta
theta_ml = max_lik_estimate(X, y)
print(theta_ml)


# Define a range of test inputs
Xtest = np.linspace(-5, 5, 100).reshape(-1, 1)

def predict_with_estimate(Xtest, theta):
    # Return predictions as dot product of test inputs and theta
    prediction = Xtest @ theta
    return prediction

# Generate predictions
ml_prediction = predict_with_estimate(Xtest, theta_ml)

# Create a plot to display data and predictions
plt.figure()
# Plot original data points
plt.plot(X, y, '+', markersize=10, label='Data points')
# Plot line of best fit
plt.plot(Xtest, ml_prediction, label=f'y={theta_ml[0][0]:.2f}x' )
plt.xlabel("X-axis ($x$)")  # Label the x-axis
plt.ylabel("Y-axis ($y$)")  # Label the y-axis
plt.title("Plot the Initial Model")  # Title for the plot
plt.xlim([-5, 5])  # Set the x-axis limits
plt.legend()  # Display legend
plt.grid(True)  # Show grid
# plt.show()  # Display the plot


# Get the shape of X
N, D = X.shape

# Augment X with a column of ones (bias term)
X_aug = np.hstack([np.ones((N, 1)), X])  # Augmented training inputs of size N x (D+1)

# Print the augmented matrix X_aug
print("=" * 10)
print("X_aug =")
print(X_aug)
print("=" * 10)

# Recalculate Theta using the augmented X
theta_aug = np.linalg.inv(X_aug.T @ X_aug) @ (X_aug.T @ y)

# Display the new Theta values
print("Theta with bias:")
print(theta_aug)


# Extend X_aug for quadratic model
X_aug_quadratic = np.hstack([np.ones((N, 1)), X, X**2])  # Augmented matrix for quadratic model

# Recalculate theta for quadratic model
theta_quadratic = np.linalg.inv(X_aug_quadratic.T @ X_aug_quadratic) @ (X_aug_quadratic.T @ y)

# Predict with the improved quadratic model
X_pred = np.linspace(-5, 5, 100).reshape(-1, 1)  # Generate a range of X values
X_pred_aug = np.hstack([np.ones((X_pred.shape[0], 1)), X_pred, X_pred**2])  # Augment for quadratic
y_pred = X_pred_aug @ theta_quadratic  # Predicted y values

# Plot the results
plt.figure()
# Plot original data points
plt.plot(X, y, '+', markersize=10, label='Data points')
# Plot quadratic model fit
plt.plot(X_pred, y_pred, label=f'$y={theta_quadratic[2][0]:.2f}x^2 + {theta_quadratic[1][0]:.2f}x + {theta_quadratic[0][0]:.2f}$', color='orange')
plt.xlabel("X-axis ($x$)")  # Label the x-axis
plt.ylabel("Y-axis ($y$)")  # Label the y-axis
plt.title("Plot of the Improved Model (Quadratic)")  # Title for the plot
plt.xlim([-5, 5])  # Set the x-axis limits
plt.legend()  # Display legend
plt.grid(True)  # Show grid
plt.show()  # Display the plot
