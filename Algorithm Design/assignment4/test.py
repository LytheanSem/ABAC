# Find sum of numbers less than the current number
def find_sum(bit, idx):
    sum_val = 0
    while idx > 0:
        sum_val += bit[idx]
        idx -= (idx & -idx)
    return sum_val

# Update the number and numbers that can use it
def update(bit, n, idx, val):
    while idx <= n:
        bit[idx] += val
        idx += (idx & -idx)

# Convert the array to a relative array (from lowest to highest) using a ranking approach
def convert(arr, n):
    temp = sorted(arr[:])
    rank = {val: idx + 1 for idx, val in enumerate(temp)}
    for i in range(n):
        arr[i] = rank[arr[i]]

# Find the number of inversions
def find_inv_count(arr, n):
    convert(arr, n)

    inv_count = 0
    bit = [0] * (n + 1)

    # Calculate inversions from right to left
    for i in range(n - 1, -1, -1):
        inv_count += find_sum(bit, arr[i] - 1)
        update(bit, n, arr[i], 1)

    return inv_count

# Input handling
import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

results = []
for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index + n]))
    index += n
    results.append(find_inv_count(arr, n))

# Output results
sys.stdout.write("\n".join(map(str, results)) + "\n")