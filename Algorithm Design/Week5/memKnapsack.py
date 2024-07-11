import sys
sys.setrecursionlimit(100000)
 
 
# Example input values
N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
 
# Initialize the recursive call counter and memoization dictionary
recursive_calls = 0
memo = {}
 
def maxVal(i, C):
    global recursive_calls
    recursive_calls += 1  # Increment the counter at each recursive call
   
    # Track the current state
    state = (i, C)
   
    # Check if the result for this state is already computed
    if state in memo:
        return memo[state]
   
    # Base case: if we have considered all items
    if i == N:
        result = 0
    else:
        skip = maxVal(i + 1, C)
        if w[i] <= C:  # w[i] does not exceed capacity
            take = v[i] + maxVal(i + 1, C - w[i])
        else:
            take = -1
        result = max(skip, take)
   
    # Memoize the result
    memo[state] = result
    return result
 
# Calculate the maximum value and print it
result = maxVal(0, M)
print("Maximum Value:", result)
 
# Print the number of recursive calls
print("Number of recursive calls:", recursive_calls)