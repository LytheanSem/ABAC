import time

start = time.process_time()

#Input the array
a = list(map(int, input().split()))
n = len(a)

#Create accumulated sum list
accumulated_sum = [0] * n
accumulated_sum[0] = a[0]
for i in range(1, n):
    accumulated_sum[i] = accumulated_sum[i - 1] + a[i]

#Modify the Sum function to use the accumulated sum list
def Sum(accumulated_sum, i, j):
    if i == 0:
        return accumulated_sum[j]
    else:
        return accumulated_sum[j] - accumulated_sum[i - 1]

#Rewrite the solution to find the maximum subarray sum
maxs = float('-inf')
for i in range(n):
    for j in range(i, n):
        maxs = max(maxs, Sum(accumulated_sum, i, j))

print("Maximum Contiguous Array Sum is", maxs)

finish = time.process_time()
print("Running time= ", finish - start)