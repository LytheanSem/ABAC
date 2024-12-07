
import numpy as np
import matplotlib.pyplot as plt

# Polynomial feature transformation function
def poly_features(X, degree):
    return np.hstack([X**i for i in range(degree + 1)])

# Maximum likelihood estimation
def maximum_likelihood(Phi, y):
    return np.linalg.inv(Phi.T @ Phi) @ Phi.T @ y

# Root Mean Square Error (RMSE) function
def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred)**2))

# Datasets: Training and Testing
X = np.array([-4.5, -3.5, -3, -1.8, -0.2, 0.3, 1.3, 2.6, 3.8, 4.8]).reshape(-1, 1)
y = np.array([-0.91650116, -0.47546053, -0.10972425, 0.29504095, -0.01596218, 
              0.10014949, 0.48104303, 0.10979023, -0.99742128, -0.91221826]).reshape(-1, 1)

X_test = np.array([-3.99, -1.38, -1.37, -0.94, 0.69, 1.4, 1.57, 1.78, 1.81, 4.89]).reshape(-1, 1)
y_test = np.array([-0.80737607, 0.19813376, 0.19537639, 0.07185977, 0.24954213, 
                   0.50662504, 0.52943298, 0.52406997, 0.51999057, -0.82318288]).reshape(-1, 1)

# Step 1: Plot the relationship between X and y
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Training Data')
plt.title("Relationship Between X and y")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

# Step 2: Transform X into polynomial features of degree 4
degree = 4
Phi_train = poly_features(X, degree)
Phi_test = poly_features(X_test, degree)

# Step 3: Estimate parameters using maximum likelihood
theta = maximum_likelihood(Phi_train, y)
print("Estimated Parameters (Theta):", theta)

# Step 4: Evaluate the model using RMSE
y_pred_train = Phi_train @ theta
y_pred_test = Phi_test @ theta
train_rmse = rmse(y, y_pred_train)
test_rmse = rmse(y_test, y_pred_test)
print("Training RMSE:", train_rmse)
print("Testing RMSE:", test_rmse)

# Calculate RMSE for polynomial degrees ranging from 0 to 15
degrees = range(0, 16)
train_rmse_values = []
test_rmse_values = []

for k in degrees:
    Phi_train_k = poly_features(X, k)
    Phi_test_k = poly_features(X_test, k)
    theta_k = maximum_likelihood(Phi_train_k, y)
    y_pred_train_k = Phi_train_k @ theta_k
    y_pred_test_k = Phi_test_k @ theta_k
    train_rmse_values.append(rmse(y, y_pred_train_k))
    test_rmse_values.append(rmse(y_test, y_pred_test_k))

# Plot RMSE vs Polynomial Degree (Step 4)
plt.figure(figsize=(8, 6))
plt.plot(degrees, train_rmse_values, marker='o', label='Training RMSE')
plt.plot(degrees, test_rmse_values, marker='s', label='Testing RMSE', linestyle='--')
plt.title("Step 4: RMSE vs Polynomial Degree (Training and Testing)")
plt.xlabel("Polynomial Degree")
plt.ylabel("RMSE")
plt.legend()
plt.grid()
plt.show()

# Step 5: RMSE Analysis and Selecting Optimal Degree
optimal_degree = 4  # Based on RMSE analysis
Phi_train_optimal = poly_features(X, optimal_degree)
theta_optimal = maximum_likelihood(Phi_train_optimal, y)

# Generate predictions for visualization
X_test_all = np.linspace(-5, 5, 100).reshape(-1, 1)
Phi_test_all = poly_features(X_test_all, optimal_degree)
y_pred_test_all = Phi_test_all @ theta_optimal

plt.figure(figsize=(8, 6))
plt.scatter(X, y, color="blue", label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Testing Data")
plt.plot(X_test_all, y_pred_test_all, color="red", label="Model Predictions")
plt.title("Step 5: Optimal Model Predictions (Degree 4)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
