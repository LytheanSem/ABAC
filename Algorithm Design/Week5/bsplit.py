a = list(map(int, input().split()))
total = sum(a)
n = len(a)

x = [0]*n

def minDiff(i):
    if i == n:
        s = 0
        for i in range(n):
            s += x[i] * a[i]
        
        m = abs(2*s - total)
        print(x, m)
        return m
    else:
        x[i] = 0
        d1 = minDiff(i+1)
        x[i] = 1
        d2 = minDiff(i+1)
        return min(d1, d2)

print(minDiff(0))