import sys
sys.setrecursionlimit(10000)  # Set recursion-stack depth

# Function to generate and count all combinations
def comb(i):
    if i == n:
        return 1  # When a complete combination is generated, return 1
    x[i] = 0  # Assign 0 to the current index
    count0 = comb(i + 1)  # Recurse to the next index and count combinations
    x[i] = 1  # Assign 1 to the current index
    count1 = comb(i + 1)  # Recurse to the next index and count combinations
    return count0 + count1  # Return the sum of both counts

# Main code
n = 3  # Example input
x = [0] * n  # Initialize the global list
total_combinations = comb(0)  # Start the recursion from the first index
print(f"Total number of combinations: {total_combinations}")  # Print the total count
