import time

def Sum(x, i, j):
    s = 0
    for k in range(i,j+1):
        s += x[k]
    return s


arr = list(map(int,input().split()))

start = time.process_time()

n = len(arr)
maxs = 0
for i in range(n):
    for j in range(i,n):
        maxs = max(maxs, Sum(arr,i,j))

print(maxs)

finish = time.process_time()
print("running time =", finish-start)