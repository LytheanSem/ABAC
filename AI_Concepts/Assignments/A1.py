import numpy as np

# Step 3: Define the matrices A and b
A = np.array([
    [1, 1, 1],
    [1, 2, 1],
    [1, 1, 2]
])

b = np.array([10, 15, 12])

# Check if the matrix is singular (determinant should not be zero)
determinant = np.linalg.det(A)
is_invertible = determinant != 0

# If invertible, compute the solution
if is_invertible:
    solution = np.linalg.solve(A, b)
else:
    solution = None

# Print results
print("Determinant:", determinant)
print("Is the matrix invertible?", is_invertible)
print("Solution (x, y, z):", solution)
