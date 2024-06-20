import sys
sys.setrecursionlimit(10000)

a = list(map(int, input().split()))

n = len(a)
x = [0]*n
minDiff = 10000000

def comb(i):
    global minDiff
    if i == n:
        s0 = s1 = 0
        for j in range(n):
            if x[j] == 0:
                s0 += a[j]
            else:
                s1 += a[j]
        minDiff = min(minDiff, abs(s0-s1))
    else:
        for j in range(2):
            x[i] = j
            comb(i+1)


comb(0)
print(minDiff)