import sys
sys.setrecursionlimit(10000)


p = list(map(int, input("Enter prices: ").split()))
L = len(p)
# count = 0
for i in range(L):
    p[i] = int(p[i])

p.insert(0,0)

calls = [0] * (1+L)
def maxRev(l):
    global p,L,calls
    # count+=1
    calls[l] += 1
    
    if l == 0:
        return 0
    else:
        mp = 0
        for i in range(1,l+1):
            mp = max(mp, p[i] + maxRev(l-i))
        return mp

print(maxRev(L))    
print(calls)
# print(f"Total recusion: {count}")

# ans to question 5 is maxRev(l) return the same value.
# ans to question 4 is L+1.
