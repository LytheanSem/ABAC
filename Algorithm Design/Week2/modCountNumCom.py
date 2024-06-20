import sys
sys.setrecursionlimit(10000)

n = int(input())
x = [0] * n

def comb(i):
    if i == n:
        #print(x)
        return 1
    else:
        x[i]=0
        a = comb(i+1)
        x[i] = 1
        b = comb(i+1)
        return a+b
    
print(comb(0))