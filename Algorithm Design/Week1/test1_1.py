import time

a = list(map(int, input().split()))
n = len(a)

start = time.process_time()
for i in range(1,n):
    a[i] += a[i-1]
    
def Sum(x, i, j):
    s = x[j]
    if i > 0:
        s -= x[i-1]
    return s

maxs = 0
for i in range(n):
    for j in range(i,n):
        maxs = max(maxs, Sum(a,i,j))
end = time.process_time()

print(maxs)
print("Time: ", end-start)