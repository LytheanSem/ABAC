p = list(map(int, input("Enter prices: ").split()))
L = len(p)
count = 0

p = [0]+p

def maxRev(l):
    global count
    count+=1
    
    if l == 0:
        return 0
    else:
        mp = 0
        for c in range(1,l+1):
                mp = max(mp, p[c] + maxRev(l-c))
        return mp
    
print(maxRev(L))    
print(f"Total recusion: {count}")
