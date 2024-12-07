import numpy as np

# Example 3x3 matrix
matrix = np.array([[3, 0, 2],
                   [2, 0, -2],
                   [0, 1, 1]])

# Calculate the determinant
det_value = np.linalg.det(matrix)
print("Determinant of the matrix:", det_value)

# Check if the matrix is invertible
if det_value != 0:
    # Compute the inverse
    inverse_matrix = np.linalg.inv(matrix)
    
    # Compute the product of the matrix and its inverse
    identity_matrix_check = np.dot(matrix, inverse_matrix)

    # Generate the expected identity matrix
    expected_identity = np.eye(matrix.shape[0])

    # Print results
    print("\nOriginal Matrix:")
    print(matrix)
    print("\nInverse Matrix:")
    print(inverse_matrix)
    print("\nProduct of Matrix and its Inverse (should be identity):")
    print(identity_matrix_check)

    # Round the product to avoid small floating-point errors
    identity_check_rounded = np.round(identity_matrix_check, 8)
    print("\nRounded Product (Identity Check):")
    print(identity_check_rounded)

    # Check if the rounded result is close to the identity matrix
    result_check = np.allclose(identity_check_rounded, expected_identity)
    print("\nIs the rounded product close to the identity matrix?", result_check)
else:
    print("The matrix is not invertible.")
