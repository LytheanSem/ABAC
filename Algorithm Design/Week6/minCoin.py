coin = list(map(int, input().split()))
V = int(input())

mm = [-1]*(V+1)

def mincoin(v):
    if mm[v] == -1:
        if v == 0:
            mm[v] = 0
        else:
            mc = 10000000000
            for c in coin:
                if c <= v:
                    mc = min(mc, 1+mincoin(v-c))
            mm[v] = mc
    return mm[v]

for v in range(V+1):
    mm[v] = mincoin(v)

print(mm[v])