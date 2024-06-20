import sys
sys.setrecursionlimit(10000)


def balance_split(i, group1_sum, group2_sum):
    if i == n:
        return abs(group1_sum - group2_sum)
    
    # Include current item in group 1
    diff1 = balance_split(i + 1, group1_sum + values[i], group2_sum)
    
    # Include current item in group 2
    diff2 = balance_split(i + 1, group1_sum, group2_sum + values[i])
    
    # Return the minimum difference
    return min(diff1, diff2)

# Main code
values = list(map(int,input().split())) # Example input
n = len(values)  # Number of items
minimal_difference = balance_split(0, 0, 0)  # Start the recursion with initial sums as 0
print(f"Minimal possible difference: {minimal_difference}")  # Print the minimal possible difference
