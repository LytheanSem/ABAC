import sys
sys.setrecursionlimit(10000)

n = int(input())
x = [0] * n

def comb(i):
    if i == n:
        #print(x)
        return 1
    else:
        s = 0
        for j in range(3):
            x[i] = j
            s += comb(i+1)
        return s

print(comb(0))