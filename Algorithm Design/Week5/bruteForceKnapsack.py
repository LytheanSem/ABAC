import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

x = [0]*N

def comb(i):    # considering item i
    if i == N:
        sw = sv = 0
        for j in range(N):
            if x[j] == 1:
                sw += w[j]
                sv += v[j]
        if sw > M:
            return -1
        else:
            return sv
    else:
        x[i] = 0
        a = comb(i+1)
        x[i] = 1
        b = comb(i+1)
        return max(a,b)
    
print(comb(0))

# ans 2: 2^i
# Accordingly, the answers of selecting item i may result in different values, yes.
# Consequently, we can't memoize this brute-force code for speed-up.