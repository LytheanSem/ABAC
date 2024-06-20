import sys
sys.setrecursionlimit(10000)

n = int(input())
k = int(input())
x = [0]*n

def comb(i):
    if i == n:
        if sum(x) == k:
            return 1
        else:
            return 0
    else:
        s = 0
        for j in range(2):
            x[i] = j
            s += comb(i+1)
        return s

print(comb(0))