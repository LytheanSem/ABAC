# Read input values
N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

# Initialize the recursive call counter
counts = 0

def maxVal(i, C):
    global counts
    counts += 1  # Increment the counter at each recursive call

    # Base case: if we have considered all items
    if i == N:
        return 0
    else:
        skip = maxVal(i + 1, C)
        if w[i] <= C:  # w[i] does not exceed capacity
            take = v[i] + maxVal(i + 1, C - w[i])
        else:
            take = -1
        return max(skip, take)

# Calculate the maximum value and print it
result = maxVal(0, M)
print("Maximum Value:", result)

# Print the number of recursive calls
print("Number of recursive calls:", counts)