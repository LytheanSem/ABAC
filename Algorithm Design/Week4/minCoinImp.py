import sys
sys.setrecursionlimit(10000)

coins = list(map(int, input().split()))
V = int(input())
calls = [0] * (V+1)
mm = [-1] * (V+1)

def mincoin(v):
    if mm[v] == -1:  
        calls[v] += 1
        if v == 0:
            mm[v] = 0
        else:
            mc = v
            for c in coins:
                if c <= v:
                    mc = min(mc, 1 + mincoin(v-c))
            mm[v] = mc
    return mm[v]
    
print(mincoin(V))
print(calls)
