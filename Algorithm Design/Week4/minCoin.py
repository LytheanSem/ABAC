import sys
sys.setrecursionlimit(10000)

coins = list(map(int, input().split()))
V = int(input())
calls = [0] * (V+1)

def mincoin(v):
    calls[v] += 1
    if v == 0:
        return 0
    else:
        mc = v
        for c in coins:
            if c <= v:
                mc = min(mc, 1 + mincoin(v-c))
        return mc
    
print(mincoin(V))
print(calls)



'''
VERY VERY IMPORTANT SO MAKE SURE YOU UNDERSTAND
Answer to q.2
=> v  minCoin(v) every coin value that is no more than the change then its correct  c<=v
=> - 1 = v-1
	3 = v-3
	4 = v-4
	5 = v-5
=> mincoin(v-1)
	mincoin(v-3)
	mincoin(v-4)
	mincoin(v-5)
=>the value of mincoin:
the minimum of this below
	mincoin(v-1)
	mincoin(v-3)
	mincoin(v-4)
	mincoin(v-5)
minimum of all of that and +1
 
=> when its 0.'''