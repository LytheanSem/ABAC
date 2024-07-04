p = list(map(int, input().split()))
L = len(p)

p = [0]+p
calls = [0] * (L+1)
mm = [-1] * [L+1]

def maxRev(l):
    if mm[l] == -1:
        calls[l] += l
        if l == 0:
            mm[l] = 0
        else:
            mp = 0
            for c in range(l,l+1):
                mp = max(mp, p[c] + maxRev(l-c))
            mm[l] == mp
    return mm[L]

print(maxRev(L))
print(calls)